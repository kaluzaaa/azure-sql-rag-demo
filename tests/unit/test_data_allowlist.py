import importlib.util
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

_spec = importlib.util.spec_from_file_location("export_data", ROOT / "scripts" / "export_data.py")
export_data = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(export_data)

# Reviewed: link slugs that episodes reference but the source repository has no file for.
KNOWN_MISSING_LINKS: set[str] = set()

EPISODE_DIRS = sorted(p for p in (DATA / "episodes").iterdir() if p.is_dir())


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _kind(path: Path) -> str | None:
    """Return the kind of a file under data/, or None when it is not expected there."""
    parts = path.relative_to(DATA).parts
    if len(parts) == 3 and parts[0] == "episodes" and re.fullmatch(r"\d{3}", parts[1]):
        return {"episode.yaml": "episode", "transcript.md": "text", "summary.md": "text"}.get(
            parts[2]
        )
    if len(parts) == 2 and parts[0] in ("links", "people") and path.suffix == ".yaml":
        return parts[0][:-1]
    return None


def test_every_file_under_data_is_expected_and_allow_listed():
    fields = {
        "episode": export_data.EPISODE_FIELDS,
        "link": export_data.LINK_FIELDS,
        "person": export_data.PERSON_FIELDS,
    }
    unexpected, violations = [], []
    for path in sorted(p for p in DATA.rglob("*") if p.is_file()):
        kind = _kind(path)
        if kind is None:
            unexpected.append(str(path.relative_to(DATA)))
        elif kind in fields:
            extra = set(_load(path)) - set(fields[kind])
            if extra:
                violations.append(f"{path.relative_to(DATA)}: {sorted(extra)}")
    assert not unexpected, f"unexpected files: {unexpected}"
    assert not violations, violations


def test_the_expected_episodes_are_exported():
    assert [int(p.name) for p in EPISODE_DIRS] == sorted(export_data.EPISODES)


@pytest.mark.parametrize("folder", EPISODE_DIRS, ids=lambda p: p.name)
def test_episode_files(folder):
    for name in ["episode.yaml", *export_data.COPIED_FILES]:
        assert (folder / name).is_file(), f"{folder.name}: missing {name}"
    episode = _load(folder / "episode.yaml")
    assert episode["episode_number"] == int(folder.name)
    assert not {"transcript", "sources", "audio", "images"} & set(episode)
    assert set(episode["ids"]) <= set(export_data.EPISODE_ID_FIELDS)


def test_referenced_links_and_guests_exist():
    missing_links, missing_guests = set(), set()
    for folder in EPISODE_DIRS:
        episode = _load(folder / "episode.yaml")
        for slug in episode.get("links", []):
            if not (DATA / "links" / f"{slug}.yaml").is_file():
                missing_links.add(slug)
        for slug in episode.get("guests", []):
            if not (DATA / "people" / f"{slug}.yaml").is_file():
                missing_guests.add(slug)
    assert missing_links == KNOWN_MISSING_LINKS
    assert not missing_guests
