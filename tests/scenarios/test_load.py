"""Given the configured database, when `demo load` runs, then it holds exactly the files in data/."""

import pytest

from demo.load import DATA, FULLTEXT_TABLES, load, read_episodes, read_folder


@pytest.fixture(scope="module")
def loaded(cursor):
    load()
    return cursor


def count(cursor, sql: str) -> int:
    cursor.execute(sql)
    return cursor.fetchone()[0]


def test_row_counts_match_the_files(loaded):
    turns = sum(len(e["turns"]) for e in read_episodes())
    assert count(loaded, "SELECT COUNT(*) FROM dbo.Episodes") == 15
    assert (
        count(loaded, "SELECT COUNT(*) FROM dbo.Links")
        == len(list((DATA / "links").glob("*.yaml")))
        == 195
    )
    assert count(loaded, "SELECT COUNT(*) FROM dbo.People") == 2
    assert count(loaded, "SELECT COUNT(*) FROM dbo.TranscriptChunks") == turns


def test_every_row_has_an_embedding(loaded):
    assert count(loaded, "SELECT COUNT(*) FROM dbo.Episodes WHERE title_embedding IS NULL") == 0
    assert count(loaded, "SELECT COUNT(*) FROM dbo.TranscriptChunks WHERE embedding IS NULL") == 0
    assert count(loaded, "SELECT COUNT(*) FROM dbo.Links WHERE embedding IS NULL") == 0


def test_fulltext_indexes_hold_every_row(loaded):
    for table in FULLTEXT_TABLES:
        indexed = count(
            loaded, f"SELECT OBJECTPROPERTYEX(OBJECT_ID('{table}'), 'TableFulltextItemCount')"
        )
        assert indexed == count(loaded, f"SELECT COUNT(*) FROM {table}"), table


def test_metadata_counts_match_the_files(loaded):
    episodes = read_episodes()
    expected = {
        "EpisodeChapters": sum(len(e.get("chapters", [])) for e in episodes),
        "EpisodeTags": sum(len(e["tags"]) for e in episodes),
        "EpisodeLinks": sum(len(e.get("links", [])) for e in episodes),
        "EpisodeGuests": sum(len(e.get("guests", [])) for e in episodes),
    }
    actual = {table: count(loaded, f"SELECT COUNT(*) FROM dbo.{table}") for table in expected}
    assert actual == expected


def row(cursor, sql: str) -> tuple:
    cursor.execute(sql)
    return tuple(cursor.fetchone())


def test_metadata_maps_known_rows(loaded):
    chapter = "SELECT start_timestamp, title FROM dbo.EpisodeChapters"
    assert row(loaded, f"{chapter} WHERE episode_number = 164 AND position = 2") == (
        "00:00:50",
        "Wprowadzenie do tematu Open Telemetry",
    )
    guest = (
        "SELECT p.name FROM dbo.EpisodeGuests g JOIN dbo.People p ON p.person_slug = g.person_slug"
    )
    assert row(loaded, f"{guest} WHERE g.episode_number = 169") == ("Bartosz Gałek",)
    link = "SELECT link_slug FROM dbo.EpisodeLinks WHERE episode_number = 164 AND position = 1"
    assert row(loaded, link) == ("opentelemetry",)
    tag = "SELECT COUNT(*) FROM dbo.EpisodeTags WHERE episode_number = 164 AND tag = 'Grafana'"
    assert row(loaded, tag) == (1,)


def test_polish_characters_survive(loaded):
    loaded.execute("SELECT name FROM dbo.People")
    names = {row[0] for row in loaded.fetchall()}
    assert names == {person["name"] for person in read_folder("people").values()}
    loaded.execute("SELECT title FROM dbo.Links")
    titles = {row[0] for row in loaded.fetchall()}
    assert titles == {link["title"] for link in read_folder("links").values()}
