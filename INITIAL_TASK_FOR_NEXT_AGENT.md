# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation (2026-11-21T10:28Z handoff)

You are the next agent. Read `AGENTS.md`, `README.md`, `PROMPT.md`, `NEXT_AGENT_TASK.md`, and `universe/last_scan.json` before acting.

## Current state
- Bound: `next_eligible_refresh_at = 2026-11-22T03:13:02.267371+00:00`
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- Snapshot: `mcap_snapshot_20261121_031302` (25/25 pages, 2500 entries, floor HTR/USDT $1,403,310)
- Universe: 280 symbols, grid 18480/18480 (280×66), 0 without fixture/cell
- Env: pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0, python 3.12.3 (temp home; re-verify/reinstall if missing)

## Your single measurable task
1. Offline first: recompute eligibility with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`). Do not guess.
2. If NOT eligible (expected until 2026-11-22T03:13:02Z): make NO provider calls. Append exactly one gate-check row to `NEXT_AGENT_TASK.md`, then stop. No wakeups.
3. If eligible: run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`). Record snapshot id, coverage, floor, `eligible_unseen_below_floor_count`, new bound. If it yields a batch, apply via the repo cycle (fixtures/grid/state/log), new symbols only, full 66-pair grid, acceptance `completed_cells == universe_n * 66`.
4. Never: rerun existing grid cells, re-fetch fixtures, fetch candles unnecessarily, place orders, change EMA/fill/cost assumptions, or blur confirmatory vs exploratory. Preserve `results/FINAL_DECISION.md`.

No provider calls before the bound. Historical research only; free public data/no-cost tooling.
EOF
echo done