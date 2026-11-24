# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-24T11:10Z (UTC). Bound `2026-11-24T14:01:08.626759+00:00` → gate **NOT ELIGIBLE** (~2h50m44s / 10,244s remaining). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261123_140108` (25/25 pages, 2500 entries, lowest rank 2500 / $1,374,604, floor `NUM/USDT` $1,385,628, `eligible_unseen_below_floor_count=0`, batch none pending). One gate-check row appended to `NEXT_AGENT_TASK.md` §4 this session (2026-11-24T11:10:24.397908+00:00).

This file is a short pointer. The canonical handoff is `INITIAL_TASK_FOR_NEXT_AGENT.md`; the full gate-check log is `NEXT_AGENT_TASK.md` §4.

## Your single measurable task

1. **Offline first:** recompute eligibility with `scripts/refresh_gate.py:gate_status(state)` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.
2. **If NOT eligible (expected until 2026-11-24T14:01:08Z):** make **no provider calls**. Append exactly one gate-check row to `NEXT_AGENT_TASK.md` §4, refresh this file's handoff time/state, then stop. Do not schedule wakeups. Each activation inside the bound records one row and nothing else.
3. **If eligible:** run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`), then apply if `EXPANSION_AVAILABLE` via repo cycle (fixtures → grid → state → log). Acceptance: `completed_cells == universe_n * 66`.

Never: rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.

## Current state (verified 2026-11-24T11:10Z)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261123_140108`, `scanned_at=2026-11-23T14:01:08.626759+00:00`, `next_eligible_refresh_at=2026-11-24T14:01:08.626759+00:00`, `coverage_reaches_below_floor=true`, lowest rank 2500 / $1,374,604, expansion floor `NUM/USDT` $1,385,628, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Universe/grid verified: `universe_n=281`, grid `results/20261019_135940_grid/progress.json` `completed_cells=18546`, `n_symbols=281`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false` (18546 == 281×66). `data/fixtures` 284 files incl. `AZERO_USDT.csv`. `universe/mcap_rank.json` n_symbols=281. `results/FINAL_DECISION.md` preserved. Git tree clean (`git status --short` empty, `git diff --stat` empty).
- Environment: `python3` 3.12.3 + `requests` 2.31.0 only — **pandas/numpy/pytest NOT importable** (`ModuleNotFoundError`, temp home wiped again). Gate tooling is stdlib-only. Reinstall `pip install --user pandas numpy pytest` before any grid/signal/pytest work.