import pytest

from demo.config import KEYS, load_settings, parse_env


def test_parse_env_skips_comments_and_strips_quotes():
    text = '# comment\n\nSQL_SERVER=s.database.windows.net\nSQL_DATABASE="db"\nnoise\n'
    assert parse_env(text) == {"SQL_SERVER": "s.database.windows.net", "SQL_DATABASE": "db"}


def test_environment_wins_over_file(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("\n".join(f"{key}=file" for key in KEYS))
    for key in KEYS:
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("SQL_DATABASE", "env")
    settings = load_settings(env_file)
    assert settings.sql_database == "env"
    assert settings.sql_server == "file"


def test_missing_settings_name_the_keys(tmp_path, monkeypatch):
    for key in KEYS:
        monkeypatch.delenv(key, raising=False)
    with pytest.raises(RuntimeError, match="FOUNDRY_ENDPOINT"):
        load_settings(tmp_path / "missing.env")
