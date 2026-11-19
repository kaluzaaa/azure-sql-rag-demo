"""Notebook helpers: run visible T-SQL on one shared connection and get a DataFrame back."""

import json
from functools import cache

import pandas as pd

from demo.db import connect
from demo.embeddings import embed

pd.set_option("display.max_colwidth", 120)  # long transcript text stays readable in tables


@cache
def _cursor():
    return connect().cursor()


def query(sql: str, params: tuple = ()) -> pd.DataFrame:
    """Run a batch and return its first result set (statements before it may return none)."""
    cursor = _cursor()
    cursor.execute(sql, params)
    while cursor.description is None and cursor.nextset():
        pass
    columns = [column[0] for column in cursor.description]
    return pd.DataFrame([tuple(row) for row in cursor.fetchall()], columns=columns)


def execute(sql: str, params: tuple = ()) -> None:
    """Run a statement that returns no rows (DDL)."""
    _cursor().execute(sql, params)


def embed_one(text: str) -> str:
    """The embedding of text as JSON, the parameter of `CAST(? AS vector(1536))`."""
    return json.dumps(embed([text])[0])
