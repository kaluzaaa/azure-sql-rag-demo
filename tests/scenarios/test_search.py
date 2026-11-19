"""Given the loaded database (test_load runs first), when the search procedures run, then
the expected episodes come first and the filters hold."""

import json
from datetime import date

import pytest

from demo.embeddings import embed

FROM_2025, TO_2025 = date(2025, 1, 1), date(2025, 12, 31)
END_2019, START_2026 = date(2019, 12, 31), date(2026, 1, 1)


def search(cursor, text: str, from_date=None, to_date=None, top_k=10, vector_text=None):
    """Run dbo.SearchChunks; the embedding is of vector_text when given, else of text."""
    cursor.execute(
        "DECLARE @e VECTOR(1536) = CAST(? AS VECTOR(1536)); "
        "EXEC dbo.SearchChunks @searchText = ?, @embedding = @e, @topK = ?, "
        "@fromDate = ?, @toDate = ?",
        json.dumps(embed([vector_text or text])[0]),
        text,
        top_k,
        from_date,
        to_date,
    )
    columns = [c[0] for c in cursor.description]
    return [dict(zip(columns, row, strict=True)) for row in cursor.fetchall()]


def count_mentions(cursor, text: str, from_date=None, to_date=None) -> list[tuple]:
    """Run dbo.CountMentions; rows are (episode_number, title, publication_date, mention_count)."""
    cursor.execute("EXEC dbo.CountMentions ?, ?, ?", text, from_date, to_date)
    return [tuple(r) for r in cursor.fetchall()]


@pytest.mark.parametrize(
    ("text", "episode"),
    [
        # Only the vector leg finds it: the transcript writes "Holmes GPT", so full-text has no match.
        ("HolmesGPT", 182),
        # All three legs rank the same turn of #10 first.
        ("vendor lock-in", 10),
    ],
)
def test_fused_search_puts_the_expected_episode_first(cursor, text, episode):
    rows = search(cursor, text)
    assert rows[0]["episode_number"] == episode, [(r["episode_number"], r["score"]) for r in rows]


def test_title_question_lands_mostly_in_its_episode(cursor):
    # "Przekonaj mnie do OpenTelemetry" is the title of #164, not a phrase of any transcript
    # (they write "Open Telemetry"), so the first turn can come from another episode;
    # #164 still has more of the top 10 than any other episode.
    rows = search(cursor, "przekonaj mnie do OpenTelemetry")
    episodes = [r["episode_number"] for r in rows]
    others = [episodes.count(e) for e in set(episodes) - {164}]
    assert episodes.count(164) > max(others, default=0), episodes


def test_date_range_returns_only_rows_inside_it(cursor):
    rows = search(cursor, "Kubernetes", FROM_2025, TO_2025)
    assert rows
    assert all(FROM_2025 <= r["publication_date"] <= TO_2025 for r in rows)


def test_each_date_bound_excludes_rows(cursor):
    unfiltered = search(cursor, "Kubernetes", top_k=150)
    assert any(not FROM_2025 <= r["publication_date"] <= TO_2025 for r in unfiltered)

    until_2019 = search(cursor, "Kubernetes", to_date=END_2019)  # only #10
    assert until_2019 and all(r["publication_date"] <= END_2019 for r in until_2019)

    from_2026 = search(cursor, "Kubernetes", from_date=START_2026)  # only #182
    assert from_2026 and all(r["publication_date"] >= START_2026 for r in from_2026)


@pytest.mark.parametrize("text", ["", "   ", "---", '""'])
def test_text_without_words_uses_only_the_vector_leg(cursor, text):
    rows = search(cursor, text, vector_text="Kubernetes")
    assert len(rows) == 10
    assert all(r["rank_vector"] and not r["rank_fulltext"] and not r["rank_phrase"] for r in rows)


def test_count_mentions_counts_2025_episodes_only(cursor):
    rows = count_mentions(cursor, "Kubernetes", FROM_2025, TO_2025)
    assert rows
    assert all(FROM_2025 <= r[2] <= TO_2025 for r in rows)


def test_count_mentions_date_bounds_exclude_rows(cursor):
    assert any(not FROM_2025 <= r[2] <= TO_2025 for r in count_mentions(cursor, "Kubernetes"))

    until_2019 = count_mentions(cursor, "Kubernetes", to_date=END_2019)  # only #10
    assert until_2019 and all(r[2] <= END_2019 for r in until_2019)

    from_2026 = count_mentions(cursor, "Kubernetes", from_date=START_2026)  # only #182
    assert from_2026 and all(r[2] >= START_2026 for r in from_2026)


@pytest.mark.parametrize("text", ["", "   ", "---", '""', "w do"])  # "w", "do": Polish stopwords
def test_count_mentions_without_searchable_words_returns_no_rows(cursor, text):
    assert count_mentions(cursor, text) == []
