# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Created:** 2026-11-27T23:04:01Z by prior agent (offline gate check only).

## State
- Gate: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `eligible_unseen_below_floor_count=0`, snapshot `mcap_snapshot_20261126_235722` (25/25 pages, 2500 entries, lowest rank 2500 / $1,326,252, coverage below floor).
- Expansion floor: SHR/USDT $1,375,627. Universe n=282, grid `completed_cells=18612` (282×66), all symbols processed, next_cell=null, stopped=false. Fixtures 284 CSV + fetch_manifest (SHR_USDT.csv present). results/FINAL_DECISION.md preserved. Git tree clean.
- Next eligible refresh bound: `2026-11-27T23:57:22.462338+00:00` (~53m remaining at creation).

## Your task (one measurable task)
1. Offline first: read this file, `NEXT_AGENT_TASK.md`, `universe/last_scan.json`. Recompute eligibility with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`). Never guess.
2. If NOT eligible (expected until 2026-11-27T23:57:22Z): make no provider calls. Append exactly one gate-check row to NEXT_AGENT_TASK.md §4 table, then stop. No wakeups, no apply, no fixtures/candles, no grid rerun.
3. If eligible: run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`). Record snapshot id, coverage (must reach below floor), floor, `eligible_unseen_below_floor_count`, new bound.
4. If that pass yields a batch (`EXPANSION_AVAILABLE`): apply via repo cycle — `refresh_universe.py fetch` (or `--apply`), then fixtures, grid, state, log — new symbols only, full 66-pair grid, descending market cap; acceptance `completed_cells == universe_n * 66`. Requires pandas installed (reinstall `pip install --user pandas numpy pytest` if missing — temp home may be wiped).
5. Never: rerun existing grid cells, re-fetch used fixtures, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, blur confirmatory vs exploratory. Preserve negative/blocked results and results/FINAL_DECISION.md. Historical research only; free public data/no-cost tooling; follow AGENTS.md adaptive gate policy.

## Env
- python 3.12.3 + requests 2.31.0 importable; pandas/numpy/pytest NOT importable this session (temp home wiped — reinstall if needed). Gate tooling is stdlib-only.
EOF
echo done