# INITIAL_TASK_FOR_NEXT_AGENT.md

**Handoff time:** 2026-11-23T03:36:51Z (UTC). **Next gate bound:** `2026-11-23T10:35:56.872136+00:00` → gate **NOT ELIGIBLE** (~6h59m06s / 25,145s remaining at handoff). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261122_103556` (25/25 pages, 2500 entries, floor `AZERO/USDT` $1,377,054, `eligible_unseen_below_floor_count=0`, batch none pending — AZERO/USDT already applied).

Universe/grid already complete and verified: `universe_n=281`, `completed_cells=18546` (281×66), `all_symbols_processed=true`, `next_cell=null`; `data/fixtures` 284 files incl. `AZERO_USDT.csv`; `universe/mcap_rank.json` n_symbols=281; `results/FINAL_DECISION.md` preserved; git tree clean.

Env this session: `python3` 3.12.3 + `requests 2.31.0` only — **pandas/numpy/pytest NOT importable** (`ModuleNotFoundError`, temp home wiped again). Gate tooling is stdlib-only and runs fine offline. Reinstall (`pip install --user pandas numpy pytest`) before any grid/signal/pytest work; `refresh_universe.py plan` also needs pandas.

## Your single measurable task — offline gate check only

Read `AGENTS.md`, `README.md`, `NEXT_AGENT_TASK.md` §4, `universe/last_scan.json`. Recompute eligibility with `scripts/refresh_gate.py:gate_status(state)` against independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess the time.

- **If NOT eligible (expected until 2026-11-23T10:35:56Z):** make **no provider calls**. Append exactly **one** gate-check row to `NEXT_AGENT_TASK.md` §4, refresh this file's handoff time/state, then stop. No wakeups, no fixtures/candles, no grid rerun, no apply. Each activation inside the bound records one row and nothing else — do not invent extra work to fill the wait.
- **If eligible:** run exactly one pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`); record snapshot id, coverage, floor, `eligible_unseen_below_floor_count`, new bound. If `EXPANSION_AVAILABLE`, apply via the repo cycle (new symbols only, full 66-pair grid; acceptance `completed_cells == universe_n * 66`).

Preserve negative/blocked results and `results/FINAL_DECISION.md`. Never change EMA signal/fill/cost assumptions, never use fixtures as market evidence, never blur confirmatory vs exploratory. Historical research only; free public data / no-cost tooling; follow the AGENTS.md adaptive gate policy.