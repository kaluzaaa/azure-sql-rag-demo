"""Prove the database features the demo needs on the real database (plan 001, task 2).

Run: uv run python scripts/check_features.py
Uses the scratch table dbo._FeatureCheck, dropped at the start and at the end.
"""

import json
import random
import sys
import time
from collections.abc import Callable
from datetime import date, timedelta

from demo.db import connect
from demo.embeddings import embed

TABLE = "dbo._FeatureCheck"
ROWS = 250
DIM = 1536
FROM_DATE, TO_DATE = date(2025, 1, 1), date(2025, 6, 30)
FULLTEXT_TIMEOUT_SECONDS = 300

results: list[tuple[str, bool, float, str]] = []


class CheckFailed(Exception):
    """A check failed; the later checks do not run."""


def unit_vector(rng: random.Random) -> list[float]:
    values = [rng.gauss(0, 1) for _ in range(DIM)]
    norm = sum(v * v for v in values) ** 0.5
    return [v / norm for v in values]


def check(name: str, body: Callable[[], str]) -> None:
    start = time.perf_counter()
    try:
        detail, passed = body(), True
    except Exception as error:  # noqa: BLE001 - report the failure, then stop
        detail, passed = f"{type(error).__name__}: {error}", False
    seconds = time.perf_counter() - start
    results.append((name, passed, seconds, detail))
    print(f"{'PASS' if passed else 'FAIL'} {name} ({seconds:.1f}s): {detail}", flush=True)
    if not passed:
        raise CheckFailed(name)


def scalar(cursor, sql: str, *params):
    cursor.execute(sql, *params)
    return cursor.fetchone()[0]


def cleanup(cursor) -> None:
    cursor.execute(f"IF OBJECT_ID('{TABLE}') IS NOT NULL DROP TABLE {TABLE}")
    cursor.execute(
        "IF EXISTS (SELECT 1 FROM sys.fulltext_catalogs WHERE name = 'FeatureCheckCatalog') "
        "DROP FULLTEXT CATALOG FeatureCheckCatalog"
    )


def run_checks(cursor) -> None:
    rng = random.Random(42)
    query = json.dumps(unit_vector(rng))

    print(
        "compatibility level:",
        scalar(cursor, "SELECT compatibility_level FROM sys.databases WHERE name = DB_NAME()"),
    )
    print(
        "service objective:",
        scalar(cursor, "SELECT DATABASEPROPERTYEX(DB_NAME(), 'ServiceObjective')"),
    )
    print("version:", scalar(cursor, "SELECT @@VERSION").splitlines()[0])

    cleanup(cursor)
    cursor.execute(
        f"""CREATE TABLE {TABLE} (
            id int NOT NULL CONSTRAINT PK_FeatureCheck PRIMARY KEY,
            published date NOT NULL,
            body nvarchar(max) NOT NULL,
            embedding vector({DIM}) NOT NULL)"""
    )

    def insert_vectors() -> str:
        start_day = date(2024, 1, 1)
        for i in range(1, ROWS + 1):
            cursor.execute(
                f"INSERT INTO {TABLE} (id, published, body, embedding) "
                f"VALUES (?, ?, ?, CAST(? AS vector({DIM})))",
                i,
                start_day + timedelta(days=3 * i),
                f"Wiersz {i}: rozmowa o chmurze.",
                json.dumps(unit_vector(rng)),
            )
        return f"{scalar(cursor, f'SELECT COUNT(*) FROM {TABLE}')} rows inserted"

    exact_ids: list[int] = []

    def exact_top10() -> str:
        cursor.execute(
            f"SELECT TOP (10) id, VECTOR_DISTANCE('cosine', embedding, CAST(? AS vector({DIM}))) AS d "
            f"FROM {TABLE} ORDER BY d",
            query,
        )
        rows = cursor.fetchall()
        assert len(rows) == 10, len(rows)
        exact_ids.extend(r[0] for r in rows)
        return f"top 10 ids {exact_ids}, best distance {rows[0][1]:.4f}"

    check(f"1a vector({DIM}) insert of {ROWS} rows", insert_vectors)
    check("1b VECTOR_DISTANCE exact top 10", exact_top10)

    def create_vector_index() -> str:
        cursor.execute(
            f"CREATE VECTOR INDEX IX_FeatureCheck_embedding ON {TABLE}(embedding) "
            "WITH (METRIC = 'cosine', TYPE = 'DiskANN')"
        )
        cursor.execute(
            "SELECT i.name, i.type_desc FROM sys.indexes i "
            f"WHERE i.object_id = OBJECT_ID('{TABLE}') AND i.name = 'IX_FeatureCheck_embedding'"
        )
        row = cursor.fetchone()
        assert row, "index not found in sys.indexes"
        return f"index {row[0]} type {row[1]}"

    check(f"2 CREATE VECTOR INDEX DiskANN on {ROWS} rows (build time)", create_vector_index)

    def approximate(where: str = "", params: tuple = ()) -> list[tuple]:
        cursor.execute(
            f"DECLARE @v vector({DIM}) = CAST(? AS vector({DIM})); "
            f"SELECT TOP (10) WITH APPROXIMATE t.id, t.published, r.distance "
            f"FROM VECTOR_SEARCH(TABLE = {TABLE} AS t, COLUMN = embedding, SIMILAR_TO = @v, "
            f"METRIC = 'cosine') AS r {where} ORDER BY r.distance",
            query,
            *params,
        )
        return cursor.fetchall()

    def vector_search() -> str:
        rows = approximate()
        assert len(rows) == 10, len(rows)
        overlap = len(set(exact_ids) & {r[0] for r in rows})
        return f"10 rows, overlap with exact top 10: {overlap}/10"

    def vector_search_filtered() -> str:
        rows = approximate("WHERE t.published BETWEEN ? AND ?", (FROM_DATE, TO_DATE))
        assert rows, "no rows"
        outside = [r for r in rows if not FROM_DATE <= r[1] <= TO_DATE]
        assert not outside, f"rows outside range: {outside}"
        return f"{len(rows)} rows, all in {FROM_DATE}..{TO_DATE}"

    check("3a VECTOR_SEARCH WITH APPROXIMATE top 10", vector_search)
    check("3b VECTOR_SEARCH with a date filter", vector_search_filtered)

    def fulltext() -> str:
        cursor.execute("SELECT lcid, name FROM sys.fulltext_languages WHERE lcid = 1045")
        print("  sys.fulltext_languages:", cursor.fetchall())
        cursor.execute(
            f"INSERT INTO {TABLE} (id, published, body, embedding) VALUES "
            f"(1001, '2025-03-01', N'Rozmawiamy o tym, jak kontenery zmieniły wdrożenia.', "
            f"CAST(? AS vector({DIM}))), "
            f"(1002, '2025-03-02', N'Vendor lock-in to temat na osobny odcinek.', "
            f"CAST(? AS vector({DIM})))",
            json.dumps(unit_vector(rng)),
            json.dumps(unit_vector(rng)),
        )
        cursor.execute(
            "IF NOT EXISTS (SELECT 1 FROM sys.fulltext_catalogs WHERE name = 'FeatureCheckCatalog') "
            "CREATE FULLTEXT CATALOG FeatureCheckCatalog"
        )
        cursor.execute(
            f"CREATE FULLTEXT INDEX ON {TABLE}(body LANGUAGE 1045) KEY INDEX PK_FeatureCheck "
            "ON FeatureCheckCatalog WITH CHANGE_TRACKING AUTO"
        )
        start = time.perf_counter()
        while True:
            cursor.execute(
                f"SELECT OBJECTPROPERTYEX(OBJECT_ID('{TABLE}'), 'TableFulltextPopulateStatus'), "
                f"OBJECTPROPERTYEX(OBJECT_ID('{TABLE}'), 'TableFulltextPendingChanges')"
            )
            status, pending = cursor.fetchone()
            if status == 0 and pending == 0:
                break
            assert time.perf_counter() - start < FULLTEXT_TIMEOUT_SECONDS, "population timeout"
            time.sleep(2)
        population = time.perf_counter() - start
        cursor.execute(
            "SELECT index_version FROM sys.fulltext_indexes WHERE object_id = OBJECT_ID(?)", TABLE
        )
        print("  sys.fulltext_indexes.index_version:", cursor.fetchone()[0])
        cursor.execute(f"SELECT [KEY], RANK FROM FREETEXTTABLE({TABLE}, body, N'kontenerów', 1045)")
        freetext = cursor.fetchall()
        assert [r[0] for r in freetext] == [1001], f"FREETEXTTABLE: {freetext}"
        cursor.execute(
            f"SELECT [KEY], RANK FROM CONTAINSTABLE({TABLE}, body, N'\"vendor lock-in\"', LANGUAGE 1045)"
        )
        phrase = cursor.fetchall()
        assert [r[0] for r in phrase] == [1002], f"CONTAINSTABLE: {phrase}"
        return (
            f"population {population:.1f}s; FREETEXTTABLE 'kontenerów' -> {freetext}; "
            f"CONTAINSTABLE phrase -> {phrase}"
        )

    check("4 Polish full-text (LCID 1045)", fulltext)

    def embedding() -> str:
        vector = embed(["Czy Azure SQL zastąpi bazę wektorową?"])[0]
        assert len(vector) == DIM and all(isinstance(v, float) for v in vector), len(vector)
        return f"{len(vector)} floats"

    check("5 embedding via demo.embeddings.embed", embedding)


def main() -> int:
    conn = connect()
    cursor = conn.cursor()
    try:
        run_checks(cursor)
    except CheckFailed:
        pass
    finally:
        cleanup(cursor)
        conn.close()

    print("\nSummary")
    for name, passed, seconds, _ in results:
        print(f"  {'PASS' if passed else 'FAIL'}  {seconds:6.1f}s  {name}")
    return 0 if all(passed for _, passed, _, _ in results) else 1


if __name__ == "__main__":
    sys.exit(main())
