# Initial Task for Next Agent — EMA Hourly Continuation

## Current State (2026-11-21T10:27Z)

- **Gate status: AWAITING_NEW_ELIGIBLE_CANDIDATES** — next eligible refresh at `2026-11-22T03:13:02.267371+00:00` (~23h42m remaining). Prior bound `2026-11-21T00:22:43.099527+00:00` ELAPSED → one ranking pass taken and the full expansion cycle applied. Latest offline gate check 2026-11-21T10:27:25Z: eligible=false, no provider calls.
- **Last snapshot:** `mcap_snapshot_20261121_031302` (25/25 pages, 2500 entries, lowest rank 2500 / $1,348,381, `coverage_reaches_below_floor=true`, `history_probe_failures=[]`).
- **Universe:** 280 symbols, grid 18,480 cells complete (280 × 66), all symbols processed; `results/20261019_135940_grid/progress.json` `completed_cells=18480`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`.
- **Expansion floor:** HTR/USDT $1,403,310; `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`.
- **Batch:** HTR/USDT applied (fixture `data/fixtures/HTR_USDT.csv` present, 22000 rows, all integrity checks OK; grid 66/66 cells 0 blocked; Batch 34 appended to `universe/mcap_expansion_log.md`).
- **Environment:** pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0, python 3.12.3 (all importable).
- **Git:** working tree clean. Prior uncommitted changes (snapshot `universe/mcap_snapshot_20261121_031302.json`, fixture `data/fixtures/HTR_USDT.csv`, grid cells `results/20261019_135940_grid/results/HTR_USDT/`, `universe/mcap_expansion_log.md` Batch 34, `universe/mcap_rank.json` 280 symbols, `universe/last_scan.json`) were committed by checkpoint `eb598d9a4e`. No new changes to commit this session (offline gate check only).

## Your Task (One Measurable Task)

1. **Offline first:** read `NEXT_AGENT_TASK.md` and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` (`2026-11-22T03:13:02.267371+00:00`) with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.

2. **If NOT eligible (expected until 2026-11-22T03:13:02Z):** make **no provider calls**. Append exactly one gate-check row to the log in `NEXT_AGENT_TASK.md` §4, then stop. Do not schedule wakeups (`cron_list` must stay empty). Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply); each activation records exactly one row and nothing else.

3. **If eligible:** run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; provider calls allowed only after the bound). Record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, new bound.

4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle — `fetch_mcap_snapshot.py --apply-from <snapshot> --apply` (no re-fetch), then `refresh_universe.py fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market cap; acceptance is `completed_cells == universe_n * 66`. Requires pandas installed.

5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow AGENTS.md adaptive gate policy.

## Key Files

- `NEXT_AGENT_TASK.md` — handoff with gate-check log (§4)
- `universe/last_scan.json` — current scan state with bound (`next_eligible_refresh_at=2026-11-22T03:13:02.267371+00:00`)
- `scripts/refresh_gate.py` — gate logic (stdlib only)
- `scripts/refresh_universe.py` — universe/grid verification cycle (needs pandas)
- `scripts/fetch_mcap_snapshot.py` — ranking pass (requests only; `--apply-from` applies without a provider call)
- `results/FINAL_DECISION.md` — confirmatory outcome (preserve)

## Environment Note

pandas/numpy/pytest are installed this session (pip --user). Re-verify imports at session start (`python3 -c "import pandas, numpy, pytest"`); reinstall with `pip install --user pandas numpy pytest` if missing before any grid/signal/pytest work. Gate tooling (`refresh_gate.py`) is stdlib-only and works without pandas.
