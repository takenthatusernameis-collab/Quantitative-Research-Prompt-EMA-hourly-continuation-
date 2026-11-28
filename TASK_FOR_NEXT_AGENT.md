# Task for Next Agent — EMA hourly continuation universe-refresh gate

**Time of handoff:** 2026-11-28T05:53:42Z (UTC). Bound `2026-11-29T05:29:55.373985+00:00` → gate **NOT ELIGIBLE** until then (~23h36m / 84,973s remaining). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261128_052955` (25/25 pages, 2500 entries, lowest rank 2500 / $1,337,581, `coverage_reaches_below_floor=true`), floor `SHR/USDT` $1,353,111, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`. Prior task COMPLETE: SHR/USDT expansion verified (grid `completed_cells=18612`=282×66, 66 SHR cells, fixture 22,099 rows) AND step-4 ranking pass already executed at 2026-11-28T05:29:55Z (0 new → AWAITING). Env: python 3.12.3 + requests 2.31.0 + pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 importable. One gate-check row appended this activation to `NEXT_AGENT_TASK.md` §4 (latest 2026-11-28T05:53:42+00:00; 330 lines total).

This file is a short pointer. The canonical handoff is `INITIAL_TASK_FOR_NEXT_AGENT.md`; the full gate-check log is `NEXT_AGENT_TASK.md` §4.

## Your single measurable task

1. **Offline first:** recompute eligibility with `scripts/refresh_gate.py:gate_status(state)` (or `scripts/refresh_universe.py plan`) vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.
2. **If NOT eligible (expected until 2026-11-29T05:29:55Z):** make **no provider calls**. Append exactly one gate-check row to `NEXT_AGENT_TASK.md` §4, refresh this file's handoff time/state and the `NEXT_AGENT_TASK.md` header, then stop. Do not schedule wakeups. Each activation inside the bound records one row and nothing else.
3. **If eligible:** run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`), then apply if `EXPANSION_AVAILABLE` via the repo cycle (`fetch_mcap_snapshot.py --apply-from <snapshot> --apply`, then `refresh_universe.py fixtures`/`grid`/`state`/`log`). Acceptance: `completed_cells == universe_n * 66`.

Never: rerun existing grid cells, re-fetch fixtures the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow AGENTS.md adaptive gate policy.