from pathlib import Path

import pytest

from demo import chunking
from demo.chunking import Turn, batches, split_turns

DATA = Path(__file__).resolve().parents[2] / "data" / "episodes"

TRANSCRIPT = """# 144.mp4

[00:00:11.02] **Szymon Warda:** Cześć, słuchacie Patoarchitektów.

[00:00:15.06] **Łukasz Kałużny:** I Łukasz Kałużny.
Druga linia tej samej wypowiedzi.

[00:00:20.00] **Szymon Warda:**

[00:00:23.10] **Tomasz Onyszko:** To prawda.
"""


def test_split_turns_keeps_speaker_timestamp_and_continuation_lines():
    assert split_turns(TRANSCRIPT) == [
        Turn(1, "Szymon Warda", "00:00:11.02", "Cześć, słuchacie Patoarchitektów."),
        Turn(
            2,
            "Łukasz Kałużny",
            "00:00:15.06",
            "I Łukasz Kałużny.\nDruga linia tej samej wypowiedzi.",
        ),
        Turn(3, "Tomasz Onyszko", "00:00:23.10", "To prawda."),
    ]


def test_split_turns_rejects_a_turn_over_the_token_limit(monkeypatch):
    monkeypatch.setattr(chunking, "MAX_TOKENS", 20)  # only the 22-token turn is over
    with pytest.raises(ValueError, match="00:00:15.06"):
        split_turns(TRANSCRIPT)


def test_every_demo_transcript_has_turns():
    for folder in sorted(DATA.iterdir()):
        assert split_turns((folder / "transcript.md").read_text(encoding="utf-8")), folder.name


def test_batches_respect_the_token_budget_and_keep_order():
    texts = ["a b c"] * 5  # 3 tokens each
    groups = list(batches(texts, max_tokens=7))
    assert [len(g) for g in groups] == [2, 2, 1]
    assert [t for g in groups for t in g] == texts


def test_batches_respect_the_input_count():
    assert [len(g) for g in batches(["a"] * 5, max_tokens=100, max_inputs=2)] == [2, 2, 1]
