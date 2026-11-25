# INITIAL TASK FOR NEXT AGENT — EMA hourly continuation universe-refresh gate

**Handoff time:** 2026-11-25T23:15:02Z (gate ELIGIBLE; ranking pass executed and applied; SHR/USDT added to universe; fixture+grid for SHR/USDT pending).

## Current state (from `universe/last_scan.json`)
- **State:** `EXPANSION_AVAILABLE`
- **Snapshot:** `mcap_snapshot_20261125_231042` (25/25 pages, 2500 entries, lowest rank 2500 / $1,329,650, `coverage_reaches_below_floor=true`)
- **Expansion floor:** `NUM/USDT` $1,374,073
- **Eligible unseen below floor:** 1 — `SHR/USDT` (ShareToken), rank 2473, $1,365,535
- **Batch selected:** `["SHR/USDT"]` — ranking already applied to `universe/mcap_rank.json` (281→282 symbols)
- **Next eligible refresh (bound):** `2026-11-26T23:10:42.705217+00:00` (~23h56m remaining)

## Universe / Grid verification
- **Universe:** 282 symbols (`universe/mcap_rank.json` n=282, SHR/USDT appended last)
- **Grid:** 18,546 completed cells (281×66, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`) at `results/20261019_135940_grid/progress.json` — SHR/USDT has **0 grid cells** (66 pending)
- **Fixtures:** 284 files in `data/fixtures/` (283 CSV + `fetch_manifest.json`) — `SHR_USDT.csv` NOT present
- **Results:** `results/FINAL_DECISION.md` preserved
- **Git:** tree modified (uncommitted): `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261125_231042.json`

## Environment
- python 3.12.3 + requests 2.31.0 importable.
- **pandas / numpy / pytest NOT importable this session** (`ModuleNotFoundError`, temp home wiped again). Gate tooling is stdlib-only and runs without them. Reinstall `pip install --user pandas numpy pytest` before any fixtures/grid/pytest work.

## Your task (one measurable task)

**SHR/USDT expansion cycle (requires pandas):**

1. **Reinstall pandas:** `pip install --user pandas numpy pytest` (verify imports). Gate stays closed until `2026-11-26T23:10:42Z` — no provider calls before then.
2. **After the bound:** run `refresh_universe.py fixtures` to download `SHR_USDT.csv` (22k hourly bars), then `refresh_universe.py grid` to run the full 66-pair EMA grid for SHR/USDT only, then `refresh_universe.py state` + `refresh_universe.py log`.
3. **Acceptance:** `results/20261019_135940_grid/progress.json` `completed_cells == universe_n * 66` (282 × 66 = 18,612), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, SHR/USDT fixture present with 66 grid cells.
4. **Then:** recompute gate eligibility with `scripts/refresh_gate.py:gate_status(state)` vs independent UTC. If NOT eligible (expected until next bound), append exactly one gate-check row to `NEXT_AGENT_TASK.md` §4, refresh handoff files, then stop. If eligible, run exactly one fetch pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`).

**Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow the AGENTS.md adaptive gate policy.
