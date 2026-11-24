# INITIAL TASK FOR NEXT AGENT — EMA hourly continuation universe-refresh gate

**Handoff time:** 2026-11-24T22:48:14Z (offline gate check completed)

## Current state (from `universe/last_scan.json`)
- **State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- **Snapshot:** `mcap_snapshot_20261124_222829` (25/25 pages, 2500 entries, lowest rank 2500 / $1,337,556, `coverage_reaches_below_floor=true`)
- **Expansion floor:** `P2P/USDT` $1,373,063 (drift from NUM/USDT $1,385,628)
- **Eligible unseen below floor:** 0
- **Batch selected:** none
- **Next eligible refresh:** `2026-11-25T22:28:29.522210+00:00` (~23h 40m from handoff)

## Universe / Grid verification
- **Universe:** 281 symbols (`universe/mcap_rank.json` n=281, updated 2026-11-22T11:03:05Z)
- **Grid:** 18,546 completed cells (18546 == 281×66, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`)
- **Fixtures:** 284 files in `data/fixtures/` incl. `AZERO_USDT.csv`
- **Results:** `results/FINAL_DECISION.md` preserved
- **Git:** modified (uncommitted): `universe/last_scan.json` + new snapshot `mcap_snapshot_20261124_222829.json`

## Environment
- pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0, python 3.12.3
- Gate tooling is stdlib-only and runs without pandas/numpy/pytest

## Your task (one measurable task)

1. **Offline first:** read `NEXT_AGENT_TASK.md` and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` (`2026-11-25T22:28:29.522210+00:00`) with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.

2. **If NOT eligible (expected until 2026-11-25T22:28:29Z):** make **no provider calls**. Append exactly one gate-check row to the log in `NEXT_AGENT_TASK.md`, then stop. Do not schedule wakeups. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply); each activation records exactly one row and nothing else.

3. **If eligible:** run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; provider calls allowed only after the bound). Record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, new bound.

4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle — `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market cap; acceptance is `completed_cells == universe_n * 66`. Requires pandas installed.

5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow the AGENTS.md adaptive gate policy.