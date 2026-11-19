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
| D14 | Explicit data first | Owner, 2026-11-19: the talk must show that explicitly extracted metadata is knowledge for the agent, and that many questions need no vector search and no full-text search at all. Notebook 3 starts with questions answered by plain SQL and shows one case where the search gives a wrong answer and `ORDER BY` gives the right one. New tables `EpisodeChapters` and `EpisodeTags` hold the metadata that `episode.yaml` already has |
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
- `EpisodeChapters(episode_number, position, start_timestamp, title)`, `EpisodeTags(episode_number, tag)` (D14); `Episodes.tags` keeps the same tags as text for the full-text index
- Full-text indexes (Polish, LCID 1045) on `TranscriptChunks.transcript_text`, `Episodes(title, summary, tags)`, `Links(title, tldr, tags)`
- `dbo.SearchChunks(@searchText, @embedding, @topK, @fromDate, @toDate, @wVector)`: three legs (Polish `FREETEXTTABLE`, exact phrase `CONTAINSTABLE`, vector) fused with RRF — a short form of production `SearchChunksFused`
- `dbo.CountMentions(@searchText, @fromDate, @toDate)`: turns per episode that hold every word

## Notebooks (45 minutes: about 20 of slides, 20 of demo, 5 of questions)

Every notebook ends each step with an assert cell, so a wrong or empty result fails the scenario test.

1. `01_vectors.ipynb` (about 6 minutes). Given the loaded database. When the cells run: create an embedding in Foundry; show the `vector` column; exact `VECTOR_DISTANCE` top 10; `CREATE VECTOR INDEX`; `VECTOR_SEARCH` with `WITH APPROXIMATE` and a date filter. Then asserts: the unfiltered searches return 10 rows each, and the filtered search returns at least one row with every row inside the date range. A cell prints the overlap of the exact and the approximate result and the timing (printed, not asserted: recall is not guaranteed).
2. `02_hybrid_search.ipynb` (about 8 minutes). When the cells run each leg alone for "HolmesGPT", "vendor lock-in" and "przekonaj mnie do OpenTelemetry", then the fused procedure. Then a table shows the rank of the expected episode per leg and after fusion. Asserts: #182 and #10 are first after fusion; for the third query #164 holds the strict majority of the top 10 (first place is a near tie with #182, because the query is the episode title, not a sentence of a transcript), and a vector search over `Episodes.title_embedding` returns #164 first — the notebook shows that a title question belongs to another embedding level.
3. `03_structured_data.ipynb` (about 6 minutes), in three parts (D14):
   - No search at all. Plain SQL answers "the latest 3 episodes", "the chapters of #164 with timestamps", "the links of #164", "the episodes with a guest and the guest's name", "episodes per tag in 2025". One contrast cell: the vector search for "najnowszy odcinek" does not return the latest episode first; `ORDER BY publication_date DESC` does. Asserts: each query returns rows; the latest episode by date is #182.
   - Search plus structure. "What did we say about Kubernetes in 2025 and with whom": `SearchChunks` with a date range, joined to `Episodes`, `EpisodeGuests` and `People`, grouped per episode with the speakers of the matching turns. Asserts: at least one row, only rows of 2025.
   - Counting. `CountMentions('Kubernetes', '2025-01-01', '2025-12-31')`: an aggregate, not a top-k list. Asserts: at least one row, only episodes of 2025.
   - Last cell: a table "question type → what answers it" (lookup, list, count, exact phrase, meaning), the same split as the production MCP tools.

## Tasks

- [x] **0. Repository skeleton.** `pyproject.toml` (uv, ruff, pytest), devcontainer, `.gitignore`, README stub. Done: `uv run ruff check . && uv run pytest` is green in a local devcontainer-equivalent run.

  Result 2026-11-19: `pyproject.toml` (uv, Python >= 3.13; `ipykernel` + `nbclient` instead of `jupyter`), devcontainer (Python 3.13 image, Azure CLI and uv features, `gitleaks` 8.30.1 release binary), `.gitignore`, README. Not run in a devcontainer yet (task 7).
- [x] **1. Infrastructure scripts.** `infra/deploy.sh` (resource group, SQL server with `--enable-ad-only-auth`, Standard S0 database, Foundry `AIServices` account, `text-embedding-3-small` deployment, role `Cognitive Services OpenAI User`, firewall rule for the caller), `firewall.sh`, `teardown.sh`. Scenario: Given `az login` on the Sponsorship subscription, when `deploy.sh` runs twice, then the second run creates nothing new (`az resource list -g <group>` returns the same ids, one role assignment) and both runs end with a readiness probe that passes: `SELECT 1` on the database and one embedding call with Entra ID, retried for up to 10 minutes (role propagation). The owner chose the paid tier and the subscription on 2026-11-19.

  Result 2026-11-19: resources in `rg-sqlragdemo-prod-001` (Sweden Central): server `sql-sqlragdemo-d8e473` (Entra-only), database `sqldb-sqlragdemo` (S0), Foundry `ai-sqlragdemo-d8e473`, deployment `text-embedding-3-small` v1 GlobalStandard capacity 50, one role assignment. `infra/names.sh` shares the names; the suffix comes from the subscription id (`NAME_SUFFIX` overrides it). The resource list was identical after runs 1, 2 and 3; runs 2 and 3 created nothing and their probe passed. The probe of run 1 (the creating run) failed on the local Mac only: the driver bundled with `mssql-python` cannot load Homebrew's OpenSSL 4 (README has the workaround; Linux is not affected). Endpoint `https://<name>.openai.azure.com/openai/v1/` with scope `https://ai.azure.com/.default` (the `cognitiveservices` host and scope work too). Codex (code): 6 defects, 5 fixed (role-assignment prerequisite, `EMBEDDING_CAPACITY`, teardown purges the soft-deleted Foundry account, the checker stops at the first failure and always cleans up); rejected: the README names `uv run demo load` before task 4 adds it. `teardown.sh` was not run.
- [x] **2. Feature check on the real database.** A script that proves on the D6 tier: `vector(1536)` column, `CREATE VECTOR INDEX` on 100+ rows, `VECTOR_SEARCH`, a Polish full-text index with a finished population, one embedding call with Entra ID. Done: all five checks pass and the plan records the results. On a failure: stop, record it, ask the owner (D6).

  Result 2026-11-19 on S0 (compatibility level 170), all checks pass: `vector(1536)` insert (250 single-row inserts 12–15 s, so the loader inserts in batches); exact `VECTOR_DISTANCE` top 10 0.1 s; `CREATE VECTOR INDEX` DiskANN on 250 rows 0.3 s; `VECTOR_SEARCH WITH APPROXIMATE` 0.1 s, overlap with the exact top 10: 10/10; the same with a date filter returns only rows in range; inserts work on a table with a vector index; Polish full-text (LCID 1045, `index_version` 2): `FREETEXTTABLE 'kontenerów'` finds "kontenery", `CONTAINSTABLE` finds the phrase, population 9–29 s; embedding call 1536 floats. D6 stays S0.
- [x] **3. Data export.** A script (kept in this repository, run against the private `episodes` checkout) that copies the D2 episodes and applies the D3 allow-list; a test asserts that every YAML file under `data/` holds only allow-listed fields. A second test scans every tracked and untracked non-ignored file (`git ls-files --cached --others --exclude-standard`) for private hosts (`docs.google.com`, `drive.google.com`, `blob.core.windows.net`, `happyscribe`), key-like strings (a `gitleaks` run with its default rules) and notebook cells with stored outputs; it also asserts that every URL under `data/` is `https` with a public host name (no IP address, no single-label host). The export script prints the list of distinct URL hosts. Done: both tests pass, and the owner reads that host list and the `data/` files before the first push.
  Result 2026-11-19: 15 episodes, 195 links, 2 people (guests exist only in #144 and #169), 1,996 turns, 1.8 MB. Tags come from `seo.tags` of the source `episode.yaml` and are exported as top-level `tags`. No missing link file. Deviations: the word `happyscribe` is not scanned (public product mentions in #175; the test asserts instead that no `episode.yaml` has `transcript`, `sources`, `audio` or `images`); the URL shape check reads only the `url` field of link files (prose in `tldr` holds fragments such as `http://localhost:8000`). Codex (code): 8 defects, 6 fixed (scan covers the export script and non-UTF-8 files, recursive allow-list over every file under `data/`, slug pattern, non-zero exit on a missing source, episode number equals folder); rejected: a public-suffix check of hosts (the owner reads the host list) and a staged export (`data/` is in git). Open: the owner reads `data/` and the list of 120 hosts before the first push (task 7).
- [x] **4. Schema and loader.** `sql/*.sql`, chunking by speaker turn (unit-tested), embeddings in batches, `uv run demo load` (idempotent: drop and recreate the demo tables), wait for full-text population. Scenario: Given an empty database, when `demo load` runs, then the row counts match the files and every chunk has an embedding.

  Result 2026-11-19: `sql/00_drop.sql`–`02_fulltext.sql`, `src/demo/chunking.py`, `load.py`, `cli.py` (`uv run demo load`). Loaded on S0: Episodes 15, TranscriptChunks 1,996, Links 195, EpisodeLinks 212, People 2, EpisodeGuests 2, EpisodeChapters 251, EpisodeTags 79; every embedding non-NULL; full-text populated when the inserts end. Load time on S0: 395 s cold (embeddings 194 s, inserts 198 s), 225 s with the git-ignored embedding cache `.cache/embeddings.json`. Deviations: inserts run row by row (`executemany` of `mssql-python` 1.18 stored "Gałek" as "Galek"; a test guards Polish characters; the 10-DTU tier is the bottleneck, a bulk insert reached 21 rows/s against 12); no turn is split (longest turn about 1,670 tokens, a turn over 8,191 raises); `max_retries=10` in `embeddings.py` for the 50K tokens-per-minute limit. Codex (code, tasks 4–5): 7 defects, 5 fixed (see task 5; exact counts and known rows in the load test); rejected: an atomic reload (a failed drop-and-reload run is fixed by running it again) and a second full load inside the test (run 3 times by hand; the test would take 8 minutes).
- [x] **5. Search procedures.** `dbo.SearchChunks`, `dbo.CountMentions`, the phrase helper function. Scenario: the three queries of notebook 2 return the expected episode first.

  Result 2026-11-19: `sql/03_functions.sql`, `sql/04_procedures.sql`; `SearchChunks` also returns `rank_fulltext`, `rank_phrase`, `rank_vector`. Fused first place: "HolmesGPT" → #182 (vector leg only: one word, no full-text hit; "Holmes GPT" hits in all three legs), "vendor lock-in" → #10 turn 87 (all legs), "przekonaj mnie do OpenTelemetry" → #182 by 0.0328 to 0.0323 over #164, which holds 8 of the top 10; the title vector search returns #164 first (distance 0.21, next 0.51) — notebook 2 and its assert changed accordingly. "najnowszy odcinek": title vector search → #175, `SearchChunks` → #141; the latest by date is #182. Kubernetes in 2025: #148, #150, #141, #168, #169; `CountMentions` → 12 episodes, all of 2025. Speakers are full names (2 hosts, 2 guests). Fixed after Codex: text without a word skips the full-text leg (`FREETEXTTABLE` errors on empty and whitespace-only text, returns 0 rows for punctuation); `CountMentions` skips `CONTAINS` on a NULL condition (SQL Server does not short-circuit it); strict-majority assert; two-sided date-bound tests. `FulltextAllWordsCondition` is simpler than production (prefix per word, no stemming). 52 tests pass against the real database (227 s).
- [x] **6. Notebooks.** The three notebooks above, outputs cleared in git. Scenario: `tests/scenarios` executes each notebook against the database without an error.

  Result 2026-11-19: three notebooks, `src/demo/notebook.py` (`query`, `execute`, `embed_one`), `tests/scenarios/test_notebooks.py`. Run time on S0: notebook 1 58 s when it builds the vector index (the build takes 47–64 s on 1,996 rows) and 5 s when the index exists; notebook 2 8.5 s; notebook 3 3.8 s. Change to D13: the index cell creates the index only when it is missing, and a labelled cell with `rebuild = False` drops it first on demand, so the speaker builds it before the talk or live; the test runs notebook 1 in both states. Measured: exact search 127 ms, `VECTOR_SEARCH` 597 ms, overlap 9/10 (question "gdzie tanio postawić mały projekt po godzinach" → #155 first); "chmura": `FREETEXT` 35 turns, `LIKE` 9. No plan assert weakened. Codex (code): 5 defects, 4 fixed (real strict majority, exact phrase-leg wording and NULL guard, content-bound Kubernetes assert, dimension check over all rows); rejected: cells that fail when run alone in a fresh kernel (a notebook runs top to bottom). Not run yet: a fresh Codespace (task 7).
- [ ] **7. Publish and dry run.** Create the public GitHub repository, push, open it in a Codespace in the browser, run README steps and all notebooks; record timings per notebook. Done: done criteria 1–4. Workspace housekeeping outside this repository: add the folder to the workspace `CLAUDE.md` table and `.gitignore`.

  Status 2026-11-19: the owner said "publikuj"; 30 unit tests (allow-lists, host scan, gitleaks) passed on a clean tree; the repository is public at https://github.com/kaluzaaa/azure-sql-rag-demo. Workspace `CLAUDE.md` and `.gitignore` list the folder. Open: the Codespace dry run. `gh codespace create` failed (the `gh` token has no `codespace` scope) and Docker is not available locally, so the devcontainer has not been built anywhere yet.

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
- 2026-11-19 owner: explicit metadata as agent knowledge, search is not always needed (D14); notebook 3 reordered, `EpisodeChapters` and `EpisodeTags` added.
