# INITIAL TASK FOR NEXT AGENT — EMA hourly continuation universe-refresh gate

**Handoff time:** 2026-11-27T05:12:10Z (gate NOT ELIGIBLE — 24 h bound `2026-11-27T23:57:22.462338+00:00`, ~18h45m12s / 67,512s remaining). Prior task is COMPLETE: SHR/USDT expansion verified AND the step-4 ranking pass already executed (0 new candidates → `AWAITING_NEW_ELIGIBLE_CANDIDATES`). Offline checks only until the bound. Env note: pandas/numpy/pytest NOT importable this session (temp home wiped again); gate tooling is stdlib-only so offline checks run without install — reinstall `pip install --user pandas numpy pytest` before any grid/signal/pytest work. Gate-check row appended this activation (2026-11-27T05:12:10Z).

## Current state (from `universe/last_scan.json`, recorded 2026-11-26T23:57:23Z)
- **State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- **Snapshot:** `mcap_snapshot_20261126_235722` (CoinGecko public API, 25/25 pages, 2500 entries, lowest rank 2500 / $1,326,252, `coverage_reaches_below_floor=true`), `fetched_at=2026-11-26T23:57:22.462338+00:00`
- **Expansion floor:** `SHR/USDT` $1,375,627
- **Eligible unseen below floor:** 0 — `batch_selected=[]` (nothing to apply)
- **Universe:** 282 symbols (`universe/mcap_rank.json` n=282, SHR/USDT appended last; this pass did NOT change the ranking)
- **Next eligible refresh (bound):** `2026-11-27T23:57:22.462338+00:00`

## Prior task completion (verified 2026-11-26T23:59:43Z)
- **SHR/USDT expansion (steps 1–3) DONE:** fixture `data/fixtures/SHR_USDT.csv` present (22,099 rows, `enough_bars`, `price_identity_ok`); grid `results/20261019_135940_grid` expanded to SHR/USDT with **66 cells** (`results/20261019_135940_grid/results/SHR_USDT/`, each with config/trades/equity/summary).
- **Grid acceptance MET:** `results/20261019_135940_grid/progress.json` `completed_cells=18612` (282×66), `n_symbols=282`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`.
- **Step-4 ranking pass DONE:** executed at `2026-11-26T23:57:22.462338+00:00` (a surviving background process from the earlier timed-out/killed attempts; this handoff made NO new provider call) → 0 eligible unseen below floor → `AWAITING_NEW_ELIGIBLE_CANDIDATES`, new bound above.
- **Results preserved:** `results/FINAL_DECISION.md` (no credible edge; program keeps expanding) unchanged.
- **Git:** tree clean except the handoff/log docs (`INITIAL_TASK_FOR_NEXT_AGENT.md`, `TASK_FOR_NEXT_AGENT.md`, `NEXT_AGENT_TASK.md`) modified/uncommitted. SHR/USDT expansion artifacts (`universe/last_scan.json`, `universe/mcap_expansion_log.md`, grid `progress.json`/`run_config.json`, `data/fixtures/fetch_manifest.json`, `data/fixtures/SHR_USDT.csv`, `results/20261019_135940_grid/results/SHR_USDT/`, `universe/mcap_snapshot_20261126_235722.json`) already committed via checkpoint.

## Environment
- python 3.12.3 + requests 2.31.0 importable. **pandas/numpy/pytest NOT importable this session** (temp home wiped again — `ModuleNotFoundError`); gate tooling (`scripts/refresh_gate.py`) is stdlib-only so offline checks run without install. Reinstall `pip install --user pandas numpy pytest` before any grid/signal/pytest work.

## Your task (one measurable task)

**Offline gate check until `2026-11-27T23:57:22Z`; one ranking pass after the bound.**

1. **Offline first:** recompute eligibility with `scripts/refresh_gate.py:gate_status(state)` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess. Read `universe/last_scan.json` for the bound.
2. **If NOT eligible (expected until 2026-11-27T23:57:22Z):** make **no provider calls**, no fixtures, no candles, no grid work. Append **exactly one** gate-check row to `NEXT_AGENT_TASK.md` §4, refresh this file's handoff time/state and the `NEXT_AGENT_TASK.md` header, then stop. Do not schedule wakeups. Each activation inside the bound records one row and nothing else.
3. **If eligible:** run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`), then record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, and the new bound.
4. **If that pass yields a batch (`EXPANSION_AVAILABLE`):** apply it through the repo cycle — `fetch_mcap_snapshot.py --apply-from <snapshot> --apply`, then `refresh_universe.py fixtures` / `grid` / `state` / `log` — new symbols only, full 66-pair grid. Acceptance: `completed_cells == universe_n * 66`. If the pass is empty (`AWAITING_NEW_ELIGIBLE_CANDIDATES`), append one gate-check row, refresh the handoff, and stop.

**Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow the AGENTS.md adaptive gate policy.