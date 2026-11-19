#!/usr/bin/env bash
# Allow the caller's current public IP on the SQL server. A re-run updates the same rule.
set -euo pipefail
# shellcheck source=infra/names.sh
source "$(dirname "$0")/names.sh"

ip="$(curl -sSf https://api.ipify.org)"
az sql server firewall-rule create -g "$RESOURCE_GROUP" -s "$SQL_SERVER_NAME" \
  -n allow-current-client --start-ip-address "$ip" --end-ip-address "$ip" -o none
echo "firewall: $SQL_SERVER_NAME allows $ip"
