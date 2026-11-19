"""Split a transcript into speaker turns, one turn per chunk, and group texts for the embeddings API.

A turn starts with a line `[HH:MM:SS.xx] **Speaker:** text`; the following lines belong to it.
The longest turn in the 15 demo transcripts has about 1,700 tokens, far below the 8,191-token
input limit of the embedding model, so a turn is never split: an oversized turn is an error.
"""

import re
from collections.abc import Iterator
from dataclasses import dataclass
from functools import cache

import tiktoken

MAX_TOKENS = 8191  # input limit of text-embedding-3-small (cl100k_base tokens)
TURN = re.compile(r"^\[(\d{2}:\d{2}:\d{2}\.\d{2,3})\]\s*\*\*(.+?):\*\*\s*(.*)$")


@dataclass(frozen=True)
class Turn:
    chunk_number: int
    speaker: str
    start_timestamp: str
    text: str


@cache
def _encoding() -> tiktoken.Encoding:
    return tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    return len(_encoding().encode(text, disallowed_special=()))


def split_turns(transcript: str) -> list[Turn]:
    """One Turn per speaker turn, numbered from 1. Text before the first turn is skipped."""
    raw: list[tuple[str, str, list[str]]] = []
    for line in transcript.splitlines():
        match = TURN.match(line.strip())
        if match:
            timestamp, speaker, first_line = match.groups()
            raw.append((timestamp, speaker.strip(), [first_line]))
        elif raw:
            raw[-1][2].append(line.strip())
    turns = []
    for timestamp, speaker, lines in raw:
        text = "\n".join(lines).strip()
        if not text:
            continue
        if count_tokens(text) > MAX_TOKENS:
            raise ValueError(f"turn at {timestamp} exceeds {MAX_TOKENS} tokens")
        turns.append(Turn(len(turns) + 1, speaker, timestamp, text))
    return turns


def batches(texts: list[str], max_tokens: int, max_inputs: int = 2048) -> Iterator[list[str]]:
    """Group texts in order so that each request stays under max_tokens and max_inputs."""
    batch: list[str] = []
    tokens = 0
    for text in texts:
        size = count_tokens(text)
        if batch and (tokens + size > max_tokens or len(batch) == max_inputs):
            yield batch
            batch, tokens = [], 0
        batch.append(text)
        tokens += size
    if batch:
        yield batch
