# Initial Task for Next Agent — EMA Hourly Continuation

## Current State (2026-11-20T22:10Z)

- **Gate status: NOT ELIGIBLE** — next eligible refresh at `2026-11-21T00:22:43.099527+00:00` (~2h12m remaining, verified via `scripts/refresh_gate.py:gate_status` vs independent UTC)
- **State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- **Last snapshot:** `mcap_snapshot_20261120_002243` (25/25 pages, 2500 entries, floor P2P/USDT $1,455,079)
- **Universe:** 279 symbols, grid 18,414 cells complete (279 × 66), all symbols processed
- **Batch:** P2P/USDT already applied (fixture `P2P_USDT.csv` present, grid expanded)
- **Environment:** pandas 3.1.1 / numpy 2.5.5 / pytest 9.2.0 + requests 2.31.0, python 3.12.3 (all importable)
- **Git:** clean

## Your Task (One Measurable Task)

1. **Offline first:** read `NEXT_AGENT_TASK.md` and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` (`2026-11-21T00:22:43.099527+00:00`) with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.

2. **If NOT eligible (expected until 2026-11-21T00:22:43Z):** make **no provider calls**. Append exactly one gate-check row to the log in `NEXT_AGENT_TASK.md`, then stop. Do not schedule wakeups. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply); each activation records exactly one row and nothing else.

3. **If eligible:** run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; provider calls allowed only after the bound). Record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, new bound.

4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle — `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market cap; acceptance is `completed_cells == universe_n * 66`. Requires pandas installed (reinstall with `pip install --user pandas numpy pytest` if missing).

5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow AGENTS.md adaptive gate policy.

## Key Files

- `NEXT_AGENT_TASK.md` — handoff with gate-check log
- `universe/last_scan.json` — current scan state with bound
- `scripts/refresh_gate.py` — gate logic (stdlib only)
- `scripts/refresh_universe.py` — universe/grid verification (needs pandas)
- `scripts/fetch_mcap_snapshot.py` — ranking pass (requests only)
- `results/FINAL_DECISION.md` — confirmatory outcome (preserve)

## Environment Note

If pandas/numpy/pytest are missing (likely — temp home may be wiped), reinstall before any grid/signal/pytest work:
```bash
pip install --user pandas numpy pytest
```
Gate tooling (`refresh_gate.py`) is stdlib-only and works without pandas.