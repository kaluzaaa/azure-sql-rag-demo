"""Readiness probe: wait until the database and the embedding deployment answer."""

import sys
import time

from demo.config import load_settings
from demo.db import connect
from demo.embeddings import embed

TIMEOUT_SECONDS = 600
PAUSE_SECONDS = 20


def check_sql() -> None:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        assert cursor.fetchone()[0] == 1


def check_embedding() -> None:
    vector = embed(["probe"])[0]
    assert len(vector) == 1536, len(vector)


def main() -> int:
    settings = load_settings()
    deadline = time.monotonic() + TIMEOUT_SECONDS
    pending = {"sql": check_sql, "embedding": check_embedding}
    while pending:
        for name, check in list(pending.items()):
            try:
                check()
                print(f"probe: {name} OK")
                del pending[name]
            except Exception as error:  # noqa: BLE001 - retry any failure until the deadline
                print(f"probe: {name} not ready: {type(error).__name__}: {str(error)[:200]}")
        if pending and time.monotonic() > deadline:
            print(f"probe: FAILED after {TIMEOUT_SECONDS}s: {sorted(pending)}")
            return 1
        if pending:
            time.sleep(PAUSE_SECONDS)
    print(f"server:   {settings.sql_server}")
    print(f"database: {settings.sql_database}")
    print(f"endpoint: {settings.foundry_endpoint}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
