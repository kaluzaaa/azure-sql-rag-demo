import pytest

from demo.config import load_settings


@pytest.fixture(scope="session")
def cursor():
    """A cursor on the real database; the scenarios skip when no database is configured."""
    try:
        load_settings()
    except RuntimeError as error:
        pytest.skip(f"no database configured: {error}")
    from demo.db import connect

    with connect() as conn:
        yield conn.cursor()
