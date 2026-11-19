# 001 — Demo repository for the talk "RAG without a vector database: Azure SQL in the lead role"

## Goal

A public repository `kaluzaaa/azure-sql-rag-demo` that the speaker opens in GitHub Codespaces in the browser and runs as Python notebooks during a 45-minute talk. An attendee can clone it, run one `az` script on their own subscription and repeat every cell.

The production system (`patoarchitekci/knowledge`, PATOMCP) stays untouched. This repository is a simplified copy of its ideas, not of its code history.

Done when:

1. `infra/deploy.sh` creates a new Azure SQL database and a Microsoft Foundry resource with an embedding deployment, with Entra ID only (no password, no API key).
2. `uv run demo load` creates the schema and loads 15 episodes from `data/` with embeddings.
3. Three notebooks run top to bottom in a fresh Codespace and their assert cells pass (`uv run pytest tests/scenarios`).
4. The repository holds no secret and no private URL: the scan of task 3 passes on every tracked file, and the owner has read the `data/` diff.

## Facts (research 2026-11-19, Microsoft Learn; URLs in the review log)

- `CREATE VECTOR INDEX` (DiskANN) and `VECTOR_SEARCH` are GA in Azure SQL Database since September 2026. Index version 3 allows writes and applies `WHERE` filters during the search. The table needs at least 100 rows with vectors. `ORDER BY` takes the distance only.
- `SELECT TOP (N) WITH APPROXIMATE … FROM VECTOR_SEARCH(TABLE = …, COLUMN = …, SIMILAR_TO = …, METRIC = 'cosine')`; without `WITH APPROXIMATE` the same function runs an exact search.
- `vector(n)`: float32 up to 1,998 dimensions; `vector(n, float16)` up to 3,996.
- No built-in hybrid search or RRF helper exists in T-SQL; Microsoft's sample also computes RRF by hand.
- `mssql-python` 1.18.0 bundles the ODBC driver and supports `Authentication=ActiveDirectoryDefault` (reuses the `az login` token). A vector parameter travels as JSON text with `CAST(? AS vector(1536))`.
- `text-embedding-3-small` in Sweden Central exists only with the `GlobalStandard` SKU.
- Codespaces has no fixed egress IP: the firewall rule is set per session.
- Not verified by any source (task 2 checks them on the real database): vector index and full-text on the Standard S0 tier; Polish full-text (LCID 1045) on a new database; the Foundry endpoint host and token scope.
- `episode.yaml` holds private fields (`sources`, `transcript.id`, `audio`, `images`). The 20 files in `data/people/` hold a name and profile links.

## Decisions

| # | Decision | Choice |
|---|---|---|
| D1 | Repository | `kaluzaaa/azure-sql-rag-demo`, public (owner, 2026-11-19) |
| D2 | Data | 15 episodes with `episode.yaml`, `transcript.md`, `summary.md`, their `links/*.yaml` and their guests' `people/*.yaml` (owner). Episodes: 10, 141, 144, 148, 150, 151, 155, 163, 164, 166, 168, 169, 173, 175, 182 |
| D3 | Published fields | Allow-lists; the export script drops everything else. `episode.yaml`: `episode_number`, `title`, `date`, `guests`, `tags`, `chapters`, `links`, `ids.youtube`, `ids.spotify`. `links/*.yaml`: `url`, `title`, `author`, `created`, `tldr`, `tags`. `people/*.yaml`: `name` only (no profile links). `transcript.md` and `summary.md` are published whole: they are the text of public podcast episodes, and the owner of the podcast decided to publish them (2026-11-19) |
| D4 | Azure | The speaker's deployment: subscription `Microsoft Azure Sponsorship`, Sweden Central, resource group `rg-sqlragdemo-prod-001` (owner). The scripts read `LOCATION`, `RESOURCE_GROUP` and `NAME_SUFFIX` from the environment (defaults: `swedencentral`, `rg-sqlragdemo`, a hash of the subscription id) and use the current `az` subscription, so an attendee runs them unchanged |
| D5 | Auth | Entra ID only: `az login` in the Codespace, `ActiveDirectoryDefault` for SQL, `DefaultAzureCredential` for Foundry (owner) |
| D6 | Database tier | Standard S0 (DTU model, 10 DTU; owner, 2026-11-19). It is billed all the time and never pauses. When task 2 fails on it: stop and ask the owner before another tier is created |
| D7 | Embeddings | `text-embedding-3-small`, 1536 dimensions, computed in Python and passed as a parameter — the same contract as production |
| D8 | Schema | Plain SQL files in `sql/`, applied in order by the loader. No Alembic, no ORM: the audience reads T-SQL |
| D9 | Guests | New tables `People` and `EpisodeGuests` (production has none), so "with whom" is a join, as the abstract promises |
| D10 | Driver | `mssql-python`; no system ODBC package |
| D11 | Language | Repository text in English; the data stays Polish |
| D12 | Out of scope | No agent or MCP server in this repository; no English copy columns; no context windows; no CI deploy. The talk can show the production MCP in Claude on a slide or live; that is not part of this plan or of the 20 demo minutes |
| D13 | Vector index | Notebook 1 owns it: `DROP INDEX IF EXISTS` then `CREATE VECTOR INDEX`. The loader creates only tables, full-text indexes, functions and procedures |

## Repository layout

| Path | Purpose |
|---|---|
| `.devcontainer/devcontainer.json` | Python 3.13, uv, Azure CLI, Jupyter and MSSQL extensions |
| `infra/deploy.sh`, `infra/firewall.sh`, `infra/teardown.sh` | Create the resources; allow the current IP; delete the resource group |
| `data/episodes/<N>/`, `data/links/`, `data/people/` | The published data (D2, D3) |
| `sql/01_tables.sql` … | Tables, full-text catalog and full-text indexes, functions, procedures (no vector index, D13) |
| `src/demo/` | `chunking.py`, `embeddings.py`, `db.py`, `load.py`, `cli.py` |
| `notebooks/01_vectors.ipynb`, `02_hybrid_search.ipynb`, `03_structured_data.ipynb` | The three demos |
| `tests/` | Unit tests for chunking; a scenario that executes the notebooks |
| `README.md` | Prerequisites first, then 4 steps: open Codespace, `az login`, `deploy.sh`, `demo load` |

## Schema (demo)

- `Episodes(episode_number PK, title, publication_date, summary, tags, youtube_id, title_embedding vector(1536))`
- `TranscriptChunks(chunk_id PK identity, episode_number FK, chunk_number, publication_date, speaker, start_timestamp, transcript_text, embedding vector(1536))` — one row per speaker turn; `publication_date` is a copy from `Episodes`, so `VECTOR_SEARCH` filters on the indexed table itself
- `Links(link_slug PK, url, title, tldr, tags, embedding vector(1536))`, `EpisodeLinks(episode_number, link_slug, position)`
- `People(person_slug PK, name)`, `EpisodeGuests(episode_number, person_slug)`
- Full-text indexes (Polish, LCID 1045) on `TranscriptChunks.transcript_text`, `Episodes(title, summary, tags)`, `Links(title, tldr, tags)`
- `dbo.SearchChunks(@searchText, @embedding, @topK, @fromDate, @toDate, @wVector)`: three legs (Polish `FREETEXTTABLE`, exact phrase `CONTAINSTABLE`, vector) fused with RRF — a short form of production `SearchChunksFused`
- `dbo.CountMentions(@searchText, @fromDate, @toDate)`: turns per episode that hold every word

## Notebooks (45 minutes: about 20 of slides, 20 of demo, 5 of questions)

Every notebook ends each step with an assert cell, so a wrong or empty result fails the scenario test.

1. `01_vectors.ipynb` (about 6 minutes). Given the loaded database. When the cells run: create an embedding in Foundry; show the `vector` column; exact `VECTOR_DISTANCE` top 10; `CREATE VECTOR INDEX`; `VECTOR_SEARCH` with `WITH APPROXIMATE` and a date filter. Then asserts: the unfiltered searches return 10 rows each, and the filtered search returns at least one row with every row inside the date range. A cell prints the overlap of the exact and the approximate result and the timing (printed, not asserted: recall is not guaranteed).
2. `02_hybrid_search.ipynb` (about 8 minutes). When the cells run each leg alone for "HolmesGPT", "vendor lock-in" and "przekonaj mnie do OpenTelemetry", then the fused procedure. Then a table shows the rank of the expected episode per leg and after fusion. Asserts: #182, #10 and #164 are first after fusion.
3. `03_structured_data.ipynb` (about 6 minutes). When the cells answer "what did we say about Kubernetes in 2025 and with whom" in SQL: semantic search with a date range, joined to `EpisodeGuests` and `People`, grouped per episode; `CountMentions('Kubernetes', '2025-01-01', '2025-12-31')`; links of the matching episodes. Asserts: every query returns at least one row and only rows of 2025; the guest join returns at least one guest name.

## Tasks

- [ ] **0. Repository skeleton.** `pyproject.toml` (uv, ruff, pytest), devcontainer, `.gitignore`, README stub. Done: `uv run ruff check . && uv run pytest` is green in a local devcontainer-equivalent run.
- [ ] **1. Infrastructure scripts.** `infra/deploy.sh` (resource group, SQL server with `--enable-ad-only-auth`, Standard S0 database, Foundry `AIServices` account, `text-embedding-3-small` deployment, role `Cognitive Services OpenAI User`, firewall rule for the caller), `firewall.sh`, `teardown.sh`. Scenario: Given `az login` on the Sponsorship subscription, when `deploy.sh` runs twice, then the second run creates nothing new (`az resource list -g <group>` returns the same ids, one role assignment) and both runs end with a readiness probe that passes: `SELECT 1` on the database and one embedding call with Entra ID, retried for up to 10 minutes (role propagation). The owner chose the paid tier and the subscription on 2026-11-19.
- [ ] **2. Feature check on the real database.** A script that proves on the D6 tier: `vector(1536)` column, `CREATE VECTOR INDEX` on 100+ rows, `VECTOR_SEARCH`, a Polish full-text index with a finished population, one embedding call with Entra ID. Done: all five checks pass and the plan records the results. On a failure: stop, record it, ask the owner (D6).
- [ ] **3. Data export.** A script (kept in this repository, run against the private `episodes` checkout) that copies the D2 episodes and applies the D3 allow-list; a test asserts that every YAML file under `data/` holds only allow-listed fields. A second test scans every tracked and untracked non-ignored file (`git ls-files --cached --others --exclude-standard`) for private hosts (`docs.google.com`, `drive.google.com`, `blob.core.windows.net`, `happyscribe`), key-like strings (a `gitleaks` run with its default rules) and notebook cells with stored outputs; it also asserts that every URL under `data/` is `https` with a public host name (no IP address, no single-label host). The export script prints the list of distinct URL hosts. Done: both tests pass, and the owner reads that host list and the `data/` files before the first push.
- [ ] **4. Schema and loader.** `sql/*.sql`, chunking by speaker turn (unit-tested), embeddings in batches, `uv run demo load` (idempotent: drop and recreate the demo tables), wait for full-text population. Scenario: Given an empty database, when `demo load` runs, then the row counts match the files and every chunk has an embedding.
- [ ] **5. Search procedures.** `dbo.SearchChunks`, `dbo.CountMentions`, the phrase helper function. Scenario: the three queries of notebook 2 return the expected episode first.
- [ ] **6. Notebooks.** The three notebooks above, outputs cleared in git. Scenario: `tests/scenarios` executes each notebook against the database without an error.
- [ ] **7. Publish and dry run.** Create the public GitHub repository, push, open it in a Codespace in the browser, run README steps and all notebooks; record timings per notebook. Done: done criteria 1–4. Workspace housekeeping outside this repository: add the folder to the workspace `CLAUDE.md` table and `.gitignore`.

## Risks for the live demo

- S0 has 10 DTU: the load and the vector index build can be slow. Task 2 measures the index build; task 7 records the timings.
- Device-code `az login` and the per-session firewall rule take about 2 minutes; do both before going on stage.
- A new role assignment needs up to 5 minutes to apply; the readiness probe of `deploy.sh` waits for it.
- 15 episodes give about 1,900 turns: the index is not faster than the exact scan at this size. The notebook says so and shows the query plan, not a speed-up.

## Review log

- 2026-11-19 research subagent (Microsoft Learn): https://learn.microsoft.com/en-us/sql/t-sql/statements/create-vector-index-transact-sql, https://learn.microsoft.com/en-us/sql/t-sql/functions/vector-search-transact-sql, https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type, https://learn.microsoft.com/en-us/azure/azure-sql/database/free-tier, https://learn.microsoft.com/en-us/sql/connect/python/mssql-python/installation, https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/embeddings, https://github.com/Azure-Samples/azure-sql-db-vector-search
- 2026-11-19 Codex (plan), 14 defects. Fixed: configurable deployment (D4), repository-wide secret scan and allow-lists for links and people (D3, task 3), people reduced to `name`, vector index ownership (D13), date range in `CountMentions`, assert cells in notebooks, owner approval before a paid tier (D6), idempotency and readiness probe of `deploy.sh`, warm-up cell, dead `AI_GENERATE_EMBEDDINGS` fact removed, production MCP demo marked as outside the plan (D12). Rejected: the workspace `CLAUDE.md`/`.gitignore` update stays (workspace rule: the map lists every sub-repository), now marked as housekeeping outside the done criteria.
- 2026-11-19 Codex (plan, second run), 4 defects, all fixed: `publication_date` on `TranscriptChunks` for the filtered `VECTOR_SEARCH`, overlap printed instead of asserted, scan covers untracked files, URL shape check plus a host list for the owner.
- 2026-11-19 owner: database tier Standard S0 instead of the free offer (D6). The warm-up cell and the resume-time measurement are removed: S0 does not pause.
