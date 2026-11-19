"""Demo settings: the environment first, then the `.env` file that `infra/deploy.sh` writes."""

import os
from dataclasses import dataclass
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parents[2] / ".env"
KEYS = ("SQL_SERVER", "SQL_DATABASE", "FOUNDRY_ENDPOINT", "EMBEDDING_DEPLOYMENT")


@dataclass(frozen=True)
class Settings:
    sql_server: str
    sql_database: str
    foundry_endpoint: str
    embedding_deployment: str


def parse_env(text: str) -> dict[str, str]:
    """Parse `KEY=value` lines; skip blanks and comments; strip optional quotes."""
    values = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def load_settings(env_file: Path = ENV_FILE) -> Settings:
    file_values = parse_env(env_file.read_text()) if env_file.exists() else {}
    values = {key: os.environ.get(key) or file_values.get(key) for key in KEYS}
    missing = [key for key, value in values.items() if not value]
    if missing:
        raise RuntimeError(f"Missing settings {missing}: run infra/deploy.sh to write {env_file}")
    return Settings(*(values[key] for key in KEYS))
