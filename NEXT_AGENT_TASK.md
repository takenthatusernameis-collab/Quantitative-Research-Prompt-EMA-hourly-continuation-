# NEXT TASK — gated universe refresh and expansion (updated 2026-10-22T08:23Z)

**Read this file first.** It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `AWAITING_NEW_ELIGIBLE_CANDIDATES` |
| Baseline grid (program grid) | `results/20261019_135940_grid` — 266 symbols × 66 pairs = 17 556 cells, complete, 0 blocked |
| Universe | N = 266, floor `AGLD/USDT` $16 279 472 |
| Frozen universe snapshot | `universe/mcap_snapshot_20261021_114120.json` (fetched 2026-10-21T11:41:20Z, 10/10 pages, 1 000 entries, lowest covered $15 931 465) |
| Last offline verification (this session) | 2026-10-22T08:23Z — `refresh_universe.py plan` → `refresh_allowed_now: false`; `refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, 0 incomplete symbols, 0 symbols without fixture/grid cells, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. `scripts/validate_fixtures.py --all`: 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows. Tests: 249 passed. **No provider call.** |
| **Next eligible universe refresh** | **2026-10-22T11:41:20Z** (24 h after the snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see `results/mutations.json`) |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`) |
| Tooling | `scripts/refresh_universe.py` (gated refresh, one command sequence) — ranking pass covers **20 pages**; `scripts/refresh_gate.py` enforces the 24 h bound |

**Provider discipline.** Until 2026-10-22T11:41:20Z the market-data provider must not be contacted at all — no polling, no "quick check", no partial refresh. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 11:41:20Z must not fetch: verify the state offline and stop cleanly. The expansion belongs to the first session that runs after the bound.

**Working directory.** Run commands from the repository root.

---

## 2. The task (execute after 2026-10-22T11:41:20Z)

### 2.1 Check the clock (offline, safe at any time)
```bash
PYTHONPATH=. python3 scripts/refresh_universe.py plan
```

### 2.2 One ranking pass, then the expansion
```bash
PYTHONPATH=. python3 scripts/refresh_universe.py fetch --pages 20 --batch-size 10
PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
PYTHONPATH=. python3 scripts/refresh_universe.py grid
PYTHONPATH=. python3 scripts/refresh_universe.py state
PYTHONPATH=. python3 scripts/refresh_universe.py log
```
Or `PYTHONPATH=. python3 scripts/refresh_universe.py all`. Key guards: `fetch` refuses before `next_eligible_refresh_at` (second pass refused), `fixtures` never re-fetches a symbol the grid already ran, `grid` expands via `--resume` skipping existing cells, `log` is idempotent and writes nothing if cycle added no name.

### 2.3 If no name is eligible below the floor
Record snapshot id, fetch time, page coverage, floor, exclusions in `universe/last_scan.json`, keep `state = AWAITING_NEW_ELIGIBLE_CANDIDATES` and set `next_eligible_refresh_at = scanned_at + 24 h`. **No section written to log** if cycle added no name.

### 2.4 If band still holds eligible names after the batch
Take remainder from same frozen snapshot (no new provider pass):
```bash
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply
PYTHONPATH=. python3 scripts/refresh_universe.py fixtures
PYTHONPATH=. python3 scripts/refresh_universe.py grid
PYTHONPATH=. python3 scripts/refresh_universe.py state
PYTHONPATH=. python3 scripts/refresh_universe.py log
```
Second batch gets its own log section (Batch 28). Order preserved.

### 2.5 After the expansion
```bash
PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid
PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid
PYTHONPATH=. python3 -m pytest tests/ -q
```
Update `universe/mcap_expansion_log.md` and this handoff. Pooled report replaced in run dir; baseline 266-symbol numbers stay in `results/mutations.json` → `parent.pooled`.

---

## 3. Acceptance checklist
- [ ] Exactly one ranking pass; snapshot committed and linked from `universe/last_scan.json`.
- [ ] Pass covered **20 pages** and snapshot records `pages_fetched == pages_requested` (truncated pass is `INCOMPLETE_SCAN`).
- [ ] `universe/mcap_rank.json` grew by exactly the batch, descending market cap, old 266 untouched.
- [ ] Fixture exists for every new symbol with ≥17 520 hourly bars, contiguous grid; `data/fixtures/fetch_manifest.json` has provenance row.
- [ ] Grid has 66 cells per new symbol: `progress.json` shows `completed_cells = (266+n)×66`, `next_cell = null`, 0 blocked.
- [ ] Fixtures of 266 existing symbols not re-fetched (row counts/spans unchanged), `universe/last_scan.json` has no `fixture_conflicts`.
- [ ] `universe/last_scan.json` reports new `universe_n`, new floor, remaining eligible count, `next_eligible_refresh_at = scanned_at + 24 h`.
- [ ] `universe/mcap_expansion_log.md` records previous N → new N, rank range, source/date **once** as `## Batch 27` (or `## Batch 28` for second batch). If no name added, log unchanged.
- [ ] `PYTHONPATH=. python3 -m pytest tests/ -q` passes.

---

## 4. What must not happen
- No provider call before 2026-10-22T11:41:20Z, no second pass inside 24 h window.
- No re-run of baseline grid, no re-opening child grid, no second worker on any run directory, no promotion from child grid.
- No re-fetch of fixture the grid already ran (invalidates stored cells). Missing fixture of gridded symbol is conflict to restore, not download.
- No change to registered grid, cost model, fill rule, folds, or §3.4 gates.
- Use `start` + `logs`/`status` for background processes (not `monitor` action to follow running processes).
