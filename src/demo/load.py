"""Load `data/` into Azure SQL: drop and create the schema, embed, insert, wait for full-text.

Every run starts from scratch, so a second run ends in the same state. Embeddings are cached
in `.cache/embeddings.json` by text hash: a reload sends only new or changed texts to Foundry.
"""

import hashlib
import json
import time
from pathlib import Path

import yaml

from demo.chunking import batches, split_turns
from demo.db import connect
from demo.embeddings import embed

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "data"
SQL = REPO / "sql"
CACHE = REPO / ".cache" / "embeddings.json"
REQUEST_TOKENS = 20_000  # per embeddings request; the deployment allows 50,000 tokens a minute
PROGRESS_EVERY = 500  # rows
FULLTEXT_TABLES = ("dbo.TranscriptChunks", "dbo.Episodes", "dbo.Links")
FULLTEXT_TIMEOUT_SECONDS = 600
TABLES = (
    "Episodes",
    "TranscriptChunks",
    "Links",
    "EpisodeLinks",
    "People",
    "EpisodeGuests",
    "EpisodeChapters",
    "EpisodeTags",
)


def read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def read_episodes() -> list[dict]:
    episodes = []
    for folder in sorted((DATA / "episodes").iterdir()):
        episode = read_yaml(folder / "episode.yaml")
        episode["summary"] = (folder / "summary.md").read_text(encoding="utf-8")
        episode["turns"] = split_turns((folder / "transcript.md").read_text(encoding="utf-8"))
        episodes.append(episode)
    return episodes


def read_folder(name: str) -> dict[str, dict]:
    return {path.stem: read_yaml(path) for path in sorted((DATA / name).glob("*.yaml"))}


def title_input(episode: dict) -> str:
    return f"Title: {episode['title']}\nTags: {', '.join(episode['tags'])}"


def link_input(link: dict) -> str:
    lines = [f"Link: {link['title']}"]
    if link.get("author"):
        lines.append(f"Author: {link['author']}")
    lines += [f"- {sentence}" for sentence in link.get("tldr", [])]
    if link.get("tags"):
        lines.append(f"Tags: {', '.join(link['tags'])}")
    return "\n".join(lines)


def text_key(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def embed_all(texts: list[str]) -> list[str]:
    """One embedding per text, as the JSON text that `CAST(? AS VECTOR(1536))` reads."""
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    missing = list(dict.fromkeys(t for t in texts if text_key(t) not in cache))
    print(f"embed: {len(texts)} texts, {len(texts) - len(missing)} cached, {len(missing)} to embed")
    done = 0
    for batch in batches(missing, REQUEST_TOKENS):
        for text, vector in zip(batch, embed(batch), strict=True):
            cache[text_key(text)] = json.dumps(vector)
        done += len(batch)
        print(f"embed: {done}/{len(missing)}", flush=True)
    if missing:
        CACHE.parent.mkdir(exist_ok=True)
        CACHE.write_text(json.dumps(cache))
    return [cache[text_key(t)] for t in texts]


def run_sql_files(cursor) -> None:
    """Run every sql/*.sql file in name order; a line `GO` separates batches."""
    for path in sorted(SQL.glob("*.sql")):
        for batch in path.read_text(encoding="utf-8").split("\nGO\n"):
            if batch.strip():
                cursor.execute(batch)
        print(f"schema: {path.name}")


def insert(cursor, table: str, rows: list[dict]) -> None:
    """Insert rows (dicts keyed by column); *embedding columns arrive as JSON text.

    One execute per row: executemany in mssql-python 1.18 binds a text column as Unicode only
    when its longest value is non-ASCII, so "Gałek" next to a longer ASCII name became "Galek".
    Rows with a vector take the row-by-row path in executemany anyway (long parameters).
    """
    columns = list(rows[0])
    values = ["CAST(? AS VECTOR(1536))" if c.endswith("embedding") else "?" for c in columns]
    sql = f"INSERT INTO dbo.{table} ({', '.join(columns)}) VALUES ({', '.join(values)})"
    for number, row in enumerate(rows, 1):
        cursor.execute(sql, tuple(row.values()))
        if number % PROGRESS_EVERY == 0 or number == len(rows):
            print(f"insert: {table} {number}/{len(rows)}", flush=True)


def wait_for_fulltext(cursor) -> None:
    """Wait until every full-text index has indexed every row of its table."""
    deadline = time.monotonic() + FULLTEXT_TIMEOUT_SECONDS
    for table in FULLTEXT_TABLES:
        while True:
            cursor.execute(
                f"SELECT OBJECTPROPERTYEX(OBJECT_ID('{table}'), 'TableFulltextPopulateStatus'), "
                f"OBJECTPROPERTYEX(OBJECT_ID('{table}'), 'TableFulltextPendingChanges'), "
                f"OBJECTPROPERTYEX(OBJECT_ID('{table}'), 'TableFulltextItemCount'), "
                f"(SELECT COUNT(*) FROM {table})"
            )
            status, pending, indexed, rows = cursor.fetchone()
            if status == 0 and pending == 0 and indexed == rows:
                print(f"fulltext: {table} {indexed}/{rows} rows indexed")
                break
            if time.monotonic() > deadline:
                raise TimeoutError(f"full-text population of {table} did not finish")
            time.sleep(2)


def load() -> None:
    started = time.perf_counter()
    episodes = read_episodes()
    links = read_folder("links")
    people = read_folder("people")

    turns = [(e, t) for e in episodes for t in e["turns"]]
    t0 = time.perf_counter()
    title_vectors = embed_all([title_input(e) for e in episodes])
    turn_vectors = embed_all([t.text for _, t in turns])
    link_vectors = embed_all([link_input(link) for link in links.values()])
    embedding_seconds = time.perf_counter() - t0

    with connect() as conn:
        cursor = conn.cursor()
        run_sql_files(cursor)

        t0 = time.perf_counter()
        insert(
            cursor,
            "Episodes",
            [
                {
                    "episode_number": e["episode_number"],
                    "title": e["title"],
                    "publication_date": e["date"],
                    "summary": e["summary"],
                    "tags": ", ".join(e["tags"]),
                    "youtube_id": e["ids"].get("youtube"),
                    "title_embedding": vector,
                }
                for e, vector in zip(episodes, title_vectors, strict=True)
            ],
        )
        insert(
            cursor,
            "TranscriptChunks",
            [
                {
                    "episode_number": e["episode_number"],
                    "chunk_number": turn.chunk_number,
                    "publication_date": e["date"],
                    "speaker": turn.speaker,
                    "start_timestamp": turn.start_timestamp,
                    "transcript_text": turn.text,
                    "embedding": vector,
                }
                for (e, turn), vector in zip(turns, turn_vectors, strict=True)
            ],
        )
        insert(
            cursor,
            "Links",
            [
                {
                    "link_slug": slug,
                    "url": link["url"],
                    "title": link["title"],
                    "author": link.get("author"),
                    "created": link.get("created"),
                    "tldr": "\n".join(link.get("tldr", [])) or None,
                    "tags": ", ".join(link.get("tags", [])) or None,
                    "embedding": vector,
                }
                for (slug, link), vector in zip(links.items(), link_vectors, strict=True)
            ],
        )
        insert(
            cursor,
            "EpisodeLinks",
            [
                {"episode_number": e["episode_number"], "link_slug": slug, "position": position}
                for e in episodes
                for position, slug in enumerate(e.get("links", []), 1)
            ],
        )
        insert(
            cursor,
            "People",
            [{"person_slug": slug, "name": person["name"]} for slug, person in people.items()],
        )
        insert(
            cursor,
            "EpisodeGuests",
            [
                {"episode_number": e["episode_number"], "person_slug": slug}
                for e in episodes
                for slug in e.get("guests", [])
            ],
        )
        insert(
            cursor,
            "EpisodeChapters",
            [
                {
                    "episode_number": e["episode_number"],
                    "position": position,
                    "start_timestamp": chapter.split(" ", 1)[0],
                    "title": chapter.split(" ", 1)[1],
                }
                for e in episodes
                for position, chapter in enumerate(e.get("chapters", []), 1)
            ],
        )
        insert(
            cursor,
            "EpisodeTags",
            [
                {"episode_number": e["episode_number"], "tag": tag}
                for e in episodes
                for tag in e["tags"]
            ],
        )
        insert_seconds = time.perf_counter() - t0

        t0 = time.perf_counter()
        wait_for_fulltext(cursor)
        fulltext_seconds = time.perf_counter() - t0

        for table in TABLES:
            cursor.execute(f"SELECT COUNT(*) FROM dbo.{table}")
            print(f"rows: {table:<17} {cursor.fetchone()[0]:>5}")

    print(
        f"time: embeddings {embedding_seconds:.0f}s, inserts {insert_seconds:.0f}s, "
        f"full-text {fulltext_seconds:.0f}s, total {time.perf_counter() - started:.0f}s"
    )
