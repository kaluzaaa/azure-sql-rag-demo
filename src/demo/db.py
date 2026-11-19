"""Azure SQL connection with Entra ID (reuses the `az login` token)."""

import mssql_python

from demo.config import load_settings


def connect() -> mssql_python.Connection:
    settings = load_settings()
    return mssql_python.connect(
        f"Server=tcp:{settings.sql_server},1433;Database={settings.sql_database};"
        "Authentication=ActiveDirectoryDefault;Encrypt=yes;TrustServerCertificate=no",
        autocommit=True,
    )
