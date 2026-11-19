"""Given the loaded database, when each notebook runs top to bottom, then no cell fails.

The assert cells inside the notebooks are the checks. Outputs are never written back.
The kernel inherits this process's environment (DYLD_LIBRARY_PATH included, when set).
"""

import time
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

NOTEBOOKS = Path(__file__).resolve().parents[2] / "notebooks"


def run(path: Path) -> None:
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook, timeout=300, kernel_name="python3", resources={"metadata": {"path": NOTEBOOKS}}
    )
    start = time.perf_counter()
    client.execute()
    print(f"{path.name}: {time.perf_counter() - start:.0f} s")


def test_vectors_notebook_without_and_with_the_index(cursor):
    cursor.execute("DROP INDEX IF EXISTS IX_TranscriptChunks_embedding ON dbo.TranscriptChunks")
    run(NOTEBOOKS / "01_vectors.ipynb")  # index absent: the notebook builds it
    run(NOTEBOOKS / "01_vectors.ipynb")  # index present: the notebook skips the build


@pytest.mark.parametrize(
    "name", ["02_hybrid_search.ipynb", "03_structured_data.ipynb"], ids=lambda name: name
)
def test_notebook_runs(cursor, name):  # cursor: skip when no database is configured
    run(NOTEBOOKS / name)
