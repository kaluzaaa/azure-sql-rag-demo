# RAG without a vector database: Azure SQL in the lead role

Demo repository for the talk. Podcast episodes live in Azure SQL Database: vectors, a DiskANN vector index, Polish full-text search and plain joins, all in T-SQL.

## Prerequisites

- An Azure subscription where you can create a resource group, an Azure SQL server and a Microsoft Foundry (AI Services) resource.
- Permission to create role assignments on the resource group: Owner, or Contributor plus User Access Administrator (or Role Based Access Control Administrator). `deploy.sh` gives you the `Cognitive Services OpenAI User` role on the Foundry resource.
- GlobalStandard quota for `text-embedding-3-small` in the chosen region (default `swedencentral`): 50K tokens per minute by default. Set `EMBEDDING_CAPACITY` (in thousands of tokens per minute) to use less.
- A GitHub account for Codespaces (or a local VS Code with Dev Containers).
- Cost: the database is Standard S0 (billed while it exists); embeddings cost cents. Run `infra/teardown.sh` when done.

## Steps

1. Open the repository in a GitHub Codespace (Code → Codespaces → Create).
2. Sign in: `az login --use-device-code` (then `az account set -s <subscription>` if needed).
3. Create the resources: `infra/deploy.sh`. It writes a git-ignored `.env` with the server, database and endpoint names (no secrets) and waits until the database and the embedding deployment answer.
4. Load the data: `uv run demo load`.

A new Codespace has a new public IP: run `infra/firewall.sh` before you connect again.

Settings for `deploy.sh` (environment variables): `LOCATION` (default `swedencentral`), `RESOURCE_GROUP` (default `rg-sqlragdemo`), `NAME_SUFFIX` (default: a short hash of the subscription id), `EMBEDDING_CAPACITY` (default `50`).

## Running on macOS outside the Codespace

The bundled SQL driver loads only OpenSSL 1.x or 3.x from `/opt/homebrew/opt/openssl`, which Homebrew now links to OpenSSL 4. Install `openssl@3` and run Python from the virtual environment with its library path (`uv run` drops this variable):

`brew install openssl@3 && DYLD_LIBRARY_PATH=$(brew --prefix openssl@3)/lib .venv/bin/python -m demo.probe`

## Notebooks

1. `notebooks/01_vectors.ipynb` — embeddings, the `vector` type, exact search, the DiskANN index, `VECTOR_SEARCH`.
2. `notebooks/02_hybrid_search.ipynb` — Polish full-text, exact phrase and vector legs, fused with RRF.
3. `notebooks/03_structured_data.ipynb` — semantic search joined with guests, dates and links.

## Clean up

`infra/teardown.sh` deletes the resource group, then purges the soft-deleted Foundry resource, so a later `deploy.sh` can reuse the same names.

Authentication is Entra ID only: no SQL password and no API key.
