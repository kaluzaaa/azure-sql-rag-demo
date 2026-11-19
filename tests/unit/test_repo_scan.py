import ipaddress
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
PRIVATE_HOSTS = ["docs.google.com", "drive.google.com", "blob.core.windows.net"]
# Files that must name the private hosts.
SCAN_EXCLUDED = {
    "tests/unit/test_repo_scan.py",
    "docs/plan/001-demo.md",
}


def _files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout.decode()
    return [f for f in out.split("\0") if f and (ROOT / f).is_file()]


def test_no_private_hosts():
    hits = []
    for rel in _files():
        if rel in SCAN_EXCLUDED:
            continue
        for number, line in enumerate((ROOT / rel).read_bytes().lower().splitlines(), 1):
            hits += [f"{rel}:{number}: {h}" for h in PRIVATE_HOSTS if h.encode() in line]
    assert not hits, "\n".join(hits)


def _bad_host(host: str | None) -> bool:
    if not host or "." not in host or host == "localhost":
        return True
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return True


def test_link_urls_are_https_with_public_hosts():
    bad = []
    for path in sorted((ROOT / "data" / "links").glob("*.yaml")):
        url = yaml.safe_load(path.read_text(encoding="utf-8")).get("url")
        parsed = urlparse(str(url))
        if parsed.scheme != "https" or _bad_host(parsed.hostname):
            bad.append(f"{path.relative_to(ROOT)}: {url}")
    assert not bad, "\n".join(bad)


def test_notebooks_have_no_stored_outputs():
    bad = []
    for rel in _files():
        if not rel.endswith(".ipynb"):
            continue
        cells = json.loads((ROOT / rel).read_text(encoding="utf-8")).get("cells", [])
        bad += [
            f"{rel}: cell {i}"
            for i, c in enumerate(cells)
            if c.get("outputs") or c.get("execution_count")
        ]
    assert not bad, "\n".join(bad)


def test_gitleaks_finds_no_secrets():
    if os.environ.get("SKIP_GITLEAKS") == "1":
        pytest.skip("SKIP_GITLEAKS=1")
    assert shutil.which("gitleaks"), "gitleaks is not installed; install it or set SKIP_GITLEAKS=1"
    with tempfile.TemporaryDirectory() as tmp:
        # Scan a copy of exactly the non-ignored files (gitleaks dir ignores .gitignore).
        for rel in _files():
            target = Path(tmp) / "tree" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, target)
        result = subprocess.run(
            ["gitleaks", "dir", str(Path(tmp) / "tree"), "--redact", "--no-banner"],
            check=False, capture_output=True, text=True,
        )
    assert result.returncode == 0, result.stdout + result.stderr
