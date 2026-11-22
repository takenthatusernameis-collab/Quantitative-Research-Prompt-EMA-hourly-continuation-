# INITIAL_TASK_FOR_NEXT_AGENT.md

Next gate bound: `2026-11-23T10:35:56.872136+00:00` (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`). Universe/grid already complete: `universe_n=281`, `completed_cells=18546` (281×66), AZERO/USDT applied (fixture + grid done), `results/FINAL_DECISION.md` preserved, git tree clean. Env has pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0.

Task: offline gate check only. Read `AGENTS.md`, `README.md`, `NEXT_AGENT_TASK.md`, `universe/last_scan.json`. Recompute eligibility via `scripts/refresh_gate.py:gate_status(state)` against independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.

- If NOT eligible (expected until 2026-11-23T10:35:56Z): make NO provider calls. Append exactly one gate-check row to `NEXT_AGENT_TASK.md` §4, then stop. No wakeups, no fixtures, no grid rerun, no apply.
- If eligible: run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`), record snapshot id, coverage, floor, `eligible_unseen_below_floor_count`, new bound. If a batch results, apply via the repo cycle (new symbols only, full 66-pair grid).

Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling.
