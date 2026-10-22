# NEXT TASK — gated universe refresh and expansion (updated 2026-10-22T10:22Z)

**Read this file first.** It supersedes prior task descriptions; the durable record of closed mutations is `results/mutations.json`.

---

## 1. Program state

| Item | Value |
|---|---|
| Program state | `AWAITING_NEW_ELIGIBLE_CANDIDATES` |
| Baseline grid (program grid) | `results/20261019_135940_grid` — 266 symbols × 66 pairs = 17 556 cells, complete, 0 blocked |
| Universe | N = 266, floor `AGLD/USDT` $16 279 472 |
| Frozen universe snapshot | `universe/mcap_snapshot_20261021_114120.json` (fetched 2026-10-21T11:41:20Z, 10/10 pages, 1 000 entries, lowest covered $15 931 465) |
| Last offline verification (this session) | 2026-10-22T10:28Z — `refresh_universe.py plan` → `refresh_allowed_now: false` (bound 2026-10-22T11:41:20Z not elapsed); `refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Tests: `249 passed`. No provider call. Next eligible refresh **2026-10-22T11:41:20Z**. |
| **Next eligible universe refresh** | **2026-10-22T11:41:20Z** (24 h after the snapshot) |
| ATR min-risk mutation | **closed: `NOT_PROMOTED`** (see `results/mutations.json`) |
| Tests | `249 passed` (`PYTHONPATH=. python3 -m pytest tests/ -q`) |
| Tooling | `scripts/refresh_universe.py` (gated refresh, one command sequence) — ranking pass covers **20 pages**; `scripts/refresh_gate.py` enforces the 24 h bound |

**Provider discipline.** Until 2026-10-22T11:41:20Z the market-data provider must not be contacted at all — no polling, no "quick check", no partial refresh. After that timestamp exactly **one** ranking pass is allowed; the new snapshot is then frozen for the following 24 h.

**Timing note.** A session that starts before 11:41:20Z must not fetch: verify the state offline and stop cleanly. The expansion belongs to the first session that runs after the bound.

**Session 2026-10-22T10:28Z (this session).** Offline only — bound not yet elapsed (10:28 < 11:41:20). `refresh_universe.py plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Outbound HTTPS confirmed against a non-provider host only. No provider contact this session (no CoinGecko, no KuCoin). `universe/last_scan.json` verification note rewritten with this session's timestamp. Session stopped cleanly; nothing was fetched. The single gated ranking pass + expansion belongs to the first session after 2026-10-22T11:41:20Z.
**Session 2026-10-22T09:52Z (this session).** Offline only — bound not yet elapsed (09:52 < 11:41:20). `plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Outbound HTTPS confirmed against a non-provider host only. No provider contact this session. The verification note in `universe/last_scan.json` was rewritten with this session's timestamp. A wakeup is scheduled for **2026-10-22T11:42:00Z** to run the single gated ranking pass + expansion once the bound opens.
**Session 2026-10-22T09:45Z.** Offline only — bound not yet elapsed (09:45 < 11:41:20). `plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. Outbound HTTPS confirmed against a non-provider host only. No provider contact this session. Session stopped cleanly; nothing was fetched.
**Session 2026-10-22T09:40Z.** Offline only — bound not yet elapsed (09:40 < 11:41:20). `plan` → `refresh_allowed_now: false`; `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps. Tests 249 passed. Outbound HTTPS confirmed (non-provider host). A wakeup is scheduled for **2026-10-22T11:42:00Z** to run the single gated ranking pass + expansion once the bound opens; no provider contact this session.
**Session 2026-10-22T08:49Z.** Offline only — bound not yet elapsed (08:49 < 11:41:20). `plan` → `refresh_allowed_now: false`; `state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Tests 249 passed. A wakeup was scheduled for 2026-10-22T11:42:00Z to run the gated expansion once the bound opens; no provider contact this session.
**Session 2026-10-22T10:50Z (this session).** Offline only — bound not yet elapsed (10:50 < 11:41:20). `refresh_universe.py plan` → `refresh_allowed_now: false` ("the 24 h refresh bound 2026-10-22T11:41:20.375553+00:00 has not elapsed yet"); `refresh_universe.py state` → N=266, floor AGLD/USDT $16 279 472, 17 556/17 556 cells, 0 blocked, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`; `scripts/validate_fixtures.py --all` → 268 fixtures, 0 invalid, 0 gaps, 0 duplicate timestamps, 0 NaN rows; `PYTHONPATH=. python3 -m pytest tests/ -q` → **249 passed**. No provider contact this session (no CoinGecko, no KuCoin). `universe/last_scan.json` verification note rewritten with this session's timestamp. Session stopped cleanly; nothing was fetched. The single gated ranking pass + expansion belongs to the first session after 2026-10-22T11:41:20Z.
**Fixture count note.** 268 fixture files on disk vs. N=266: the two extras are `CCD/USDT` and `sample_hourly`. `sample_hourly` is the synthetic template used by `scripts/run_baseline.py` / `scripts/cost_stress.py` (no manifest row). `CCD/USDT` (Concordium) is **eligible but above the expansion floor** — snapshot rank 552, $41 673 734, tradable KuCoin pair, its fixture is pre-fetched and valid (22 099 rows) — and it was deliberately kept out of the universe by the strict append-only rule of PROMPT.md §2.1.2 (documented in `universe/mcap_expansion_log.md`, "Names deliberately skipped", together with `GAS`, rank 322, $82 731 692). Both have no grid cells and enter the universe only if a later snapshot puts them below the floor. Neither is in `universe/mcap_rank.json`, so neither is ever re-fetched or re-gridded. `data/fixtures/fetch_manifest.json` has 267 rows (266 universe symbols + CCD; the template has none).

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
