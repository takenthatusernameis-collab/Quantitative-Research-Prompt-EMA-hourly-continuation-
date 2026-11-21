# Initial task for next agent

Gate is NOT eligible until 2026-11-22T03:13:02.267371+00:00. Bound not elapsed as of this handoff.

Your task:
1. Recompute eligibility with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`). Never guess.
2. If NOT eligible (expected): make no provider calls. Append exactly one gate-check row to `NEXT_AGENT_TASK.md` §4 log, then stop. Do not schedule wakeups.
3. If eligible: run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`). Record snapshot id, coverage (must reach below floor), floor, `eligible_unseen_below_floor_count`, new bound.
4. If that pass yields a batch (`EXPANSION_AVAILABLE`): apply through repo cycle — `refresh_universe.py fetch`, then `fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid; acceptance `completed_cells == universe_n * 66`. Requires pandas installed.
5. Never rerun existing grid cells, re-fetch fixtures, fetch candles unnecessarily, place orders, change EMA/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling.

Current state: universe 280 / grid 18480/18480 complete (280×66). Env: pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0, python 3.12.3. No wakeups scheduled.
" filePath">
/home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-/INITIAL_TASK_FOR_NEXT_AGENT.md