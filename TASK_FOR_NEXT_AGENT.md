# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-23T03:48:59Z (UTC). Bound `2026-11-23T10:35:56.872136+00:00` → gate **NOT ELIGIBLE** (~6h47m remaining). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261122_103556` (25/25 pages, 2500 entries, floor `AZERO/USDT` $1,377,054, `eligible_unseen_below_floor_count=0`, batch none pending — AZERO/USDT already applied). Expansion already applied: universe 280 → 281 (AZERO/USDT added), grid 18546/18546 complete, new bound set. One offline gate-check row appended to `NEXT_AGENT_TASK.md` §4 this session.

This file is a short pointer. The canonical handoff is `INITIAL_TASK_FOR_NEXT_AGENT.md`; the full gate-check log is `NEXT_AGENT_TASK.md` §4.

## Your single measurable task

1. **Offline first:** recompute eligibility with `scripts/refresh_gate.py:gate_status(state)` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.
2. **If NOT eligible (expected until 2026-11-23T10:35:56Z):** make **no provider calls**. Append exactly one gate-check row to `NEXT_AGENT_TASK.md` §4, refresh this file's handoff time/state, then stop. Do not schedule wakeups. Each activation inside the bound records one row and nothing else.
3. **If eligible:** run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`), then apply if `EXPANSION_AVAILABLE` via repo cycle (fixtures → grid → state → log). Acceptance: `completed_cells == universe_n * 66`.

Never: rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.

## Current state (verified 2026-11-23T03:48:59Z)

- `universe/last_scan.json`: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261122_103556`, `next_eligible_refresh_at=2026-11-23T10:35:56.872136+00:00`.
- Universe/grid verified: `universe_n=281`, grid `completed_cells=18546`, `n_symbols=281`, `all_symbols_processed=true` (18546 == 281×66). `data/fixtures` 284 files incl. `AZERO_USDT.csv`. `universe/mcap_rank.json` n_symbols=281. `results/FINAL_DECISION.md` preserved. Git tree clean.
- Environment: `python3` 3.12.3 + `requests 2.31.0` only — **pandas/numpy/pytest NOT importable** this session (temp home wiped again). Gate tooling is stdlib-only. Reinstall `pip install --user pandas numpy pytest` before any grid/signal/pytest work.