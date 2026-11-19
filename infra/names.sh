# shellcheck shell=bash disable=SC2034
# Resource names shared by the infra scripts. Source it; do not run it.
# Override any value with an environment variable.

LOCATION="${LOCATION:-swedencentral}"
RESOURCE_GROUP="${RESOURCE_GROUP:-rg-sqlragdemo}"
SUBSCRIPTION_ID="$(az account show --query id -o tsv)"
NAME_SUFFIX="${NAME_SUFFIX:-$(printf '%s' "$SUBSCRIPTION_ID" | shasum | cut -c1-6)}"

SQL_SERVER_NAME="sql-sqlragdemo-${NAME_SUFFIX}"
SQL_DATABASE="sqldb-sqlragdemo"
FOUNDRY_NAME="ai-sqlragdemo-${NAME_SUFFIX}"
EMBEDDING_DEPLOYMENT="text-embedding-3-small"
