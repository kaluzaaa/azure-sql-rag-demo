"""Export the demo data from the private `episodes` checkout.

Usage: uv run python scripts/export_data.py <path-to-episodes-data>

Recreates data/episodes, data/links and data/people. Only allow-listed fields
are written (plan D3). Episode tags come from `seo.tags` in the source file.
"""

import re
import shutil
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import yaml

EPISODES = [10, 141, 144, 148, 150, 151, 155, 163, 164, 166, 168, 169, 173, 175, 182]

EPISODE_FIELDS = ["episode_number", "title", "date", "guests", "tags", "chapters", "links", "ids"]
EPISODE_ID_FIELDS = ["youtube", "spotify"]
LINK_FIELDS = ["url", "title", "author", "created", "tldr", "tags"]
PERSON_FIELDS = ["name"]
COPIED_FILES = ["transcript.md", "summary.md"]

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
SLUG = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8"
    )


def check_slug(slug: str) -> str:
    if not isinstance(slug, str) or not SLUG.fullmatch(slug):
        raise ValueError(f"invalid slug: {slug!r}")
    return slug


def pick(source: dict, fields: list[str]) -> dict:
    return {f: source[f] for f in fields if source.get(f) is not None}


def export_episode(src: Path, dst: Path) -> dict:
    source = load(src / "episode.yaml")
    if source["episode_number"] != int(src.name):
        raise ValueError(f"{src.name}: episode_number is {source['episode_number']}")
    source["tags"] = (source.get("seo") or {}).get("tags")
    episode = pick(source, EPISODE_FIELDS)
    episode["ids"] = pick(source.get("ids") or {}, EPISODE_ID_FIELDS)
    dump(episode, dst / "episode.yaml")
    for name in COPIED_FILES:
        shutil.copyfile(src / name, dst / name)
    return episode


def main(source_root: Path) -> None:
    for kind in ("episodes", "links", "people"):
        shutil.rmtree(DATA / kind, ignore_errors=True)
        (DATA / kind).mkdir(parents=True)

    link_slugs: list[str] = []
    guest_slugs: list[str] = []
    for number in EPISODES:
        folder = f"{number:03d}"
        episode = export_episode(source_root / "episodes" / folder, DATA / "episodes" / folder)
        link_slugs += map(check_slug, episode.get("links", []))
        guest_slugs += map(check_slug, episode.get("guests", []))

    missing = []
    missing_people = []
    hosts: Counter[str] = Counter()
    for slug in sorted(set(link_slugs)):
        src = source_root / "links" / f"{slug}.yaml"
        if not src.exists():
            missing.append(slug)
            continue
        link = pick(load(src), LINK_FIELDS)
        dump(link, DATA / "links" / f"{slug}.yaml")
        hosts[urlparse(link.get("url", "")).hostname or "(none)"] += 1
    for slug in sorted(set(guest_slugs)):
        dump(
            pick(load(source_root / "people" / f"{slug}.yaml"), PERSON_FIELDS),
            DATA / "people" / f"{slug}.yaml",
        )

    print(f"episodes: {len(EPISODES)}")
    print(f"links: {len(set(link_slugs)) - len(missing)} (referenced {len(set(link_slugs))})")
    print(f"people: {len(set(guest_slugs)) - len(missing_people)}")
    for slug in missing:
        print(f"ERROR: link slug without a source file: {slug}")
    for slug in missing_people:
        print(f"ERROR: guest slug without a source file: {slug}")
    print("URL hosts:")
    for host, count in sorted(hosts.items()):
        print(f"  {host}: {count}")
    if missing or missing_people:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(Path(sys.argv[1]))
