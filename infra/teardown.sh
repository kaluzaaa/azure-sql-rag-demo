#!/usr/bin/env bash
# Delete the demo resource group after a typed confirmation.
set -euo pipefail
# shellcheck source=infra/names.sh
source "$(dirname "$0")/names.sh"

echo "This deletes resource group '$RESOURCE_GROUP' in subscription '$(az account show --query name -o tsv)'."
read -r -p "Type the resource group name to confirm: " answer
if [ "$answer" != "$RESOURCE_GROUP" ]; then
  echo "Not confirmed. Nothing deleted."
  exit 1
fi

az group delete -n "$RESOURCE_GROUP" --yes
echo "Deleted $RESOURCE_GROUP."

# A deleted Foundry account stays soft-deleted and keeps its name; purge it so deploy.sh can reuse it.
az cognitiveservices account purge -g "$RESOURCE_GROUP" -n "$FOUNDRY_NAME" -l "$LOCATION"
echo "Purged the soft-deleted Foundry account $FOUNDRY_NAME."
