#!/usr/bin/env bash
# Create the demo resources in the current az subscription. Safe to run again.
set -euo pipefail
cd "$(dirname "$0")/.."
# shellcheck source=infra/names.sh
source infra/names.sh

USER_NAME="$(az account show --query user.name -o tsv)"
USER_ID="$(az ad signed-in-user show --query id -o tsv)"
ROLE="Cognitive Services OpenAI User"
EMBEDDING_CAPACITY="${EMBEDDING_CAPACITY:-50}"  # thousands of tokens per minute

echo "subscription: $(az account show --query name -o tsv)"
echo "resource group: $RESOURCE_GROUP ($LOCATION), suffix: $NAME_SUFFIX"

exists() { "$@" -o none 2>/dev/null; }

az group create -n "$RESOURCE_GROUP" -l "$LOCATION" -o none

if ! exists az sql server show -g "$RESOURCE_GROUP" -n "$SQL_SERVER_NAME"; then
  echo "creating SQL server $SQL_SERVER_NAME"
  az sql server create -g "$RESOURCE_GROUP" -n "$SQL_SERVER_NAME" -l "$LOCATION" \
    --enable-ad-only-auth --external-admin-principal-type User \
    --external-admin-name "$USER_NAME" --external-admin-sid "$USER_ID" -o none
fi

if ! exists az sql db show -g "$RESOURCE_GROUP" -s "$SQL_SERVER_NAME" -n "$SQL_DATABASE"; then
  echo "creating database $SQL_DATABASE (Standard S0)"
  az sql db create -g "$RESOURCE_GROUP" -s "$SQL_SERVER_NAME" -n "$SQL_DATABASE" \
    --service-objective S0 -o none
fi

infra/firewall.sh

if ! exists az cognitiveservices account show -g "$RESOURCE_GROUP" -n "$FOUNDRY_NAME"; then
  echo "creating Foundry account $FOUNDRY_NAME"
  az cognitiveservices account create -g "$RESOURCE_GROUP" -n "$FOUNDRY_NAME" -l "$LOCATION" \
    --kind AIServices --sku S0 --custom-domain "$FOUNDRY_NAME" --yes -o none
fi

if ! exists az cognitiveservices account deployment show -g "$RESOURCE_GROUP" -n "$FOUNDRY_NAME" \
  --deployment-name "$EMBEDDING_DEPLOYMENT"; then
  echo "creating deployment $EMBEDDING_DEPLOYMENT"
  az cognitiveservices account deployment create -g "$RESOURCE_GROUP" -n "$FOUNDRY_NAME" \
    --deployment-name "$EMBEDDING_DEPLOYMENT" --model-name text-embedding-3-small \
    --model-version 1 --model-format OpenAI --sku-name GlobalStandard --sku-capacity "$EMBEDDING_CAPACITY" -o none
fi

FOUNDRY_ID="$(az cognitiveservices account show -g "$RESOURCE_GROUP" -n "$FOUNDRY_NAME" --query id -o tsv)"
if [ -z "$(az role assignment list --assignee "$USER_ID" --role "$ROLE" --scope "$FOUNDRY_ID" --query "[].id" -o tsv)" ]; then
  echo "assigning role $ROLE"
  az role assignment create --assignee-object-id "$USER_ID" --assignee-principal-type User \
    --role "$ROLE" --scope "$FOUNDRY_ID" -o none
fi

cat > .env <<ENV
SQL_SERVER=${SQL_SERVER_NAME}.database.windows.net
SQL_DATABASE=${SQL_DATABASE}
FOUNDRY_ENDPOINT=https://${FOUNDRY_NAME}.openai.azure.com/openai/v1/
EMBEDDING_DEPLOYMENT=${EMBEDDING_DEPLOYMENT}
ENV
echo "wrote .env"

uv run python -u -m demo.probe
