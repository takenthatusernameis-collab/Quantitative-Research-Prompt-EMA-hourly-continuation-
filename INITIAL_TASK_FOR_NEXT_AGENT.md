# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Generated:** 2026-11-28T13:47:08Z (this session appended one gate-check row to `NEXT_AGENT_TASK.md` §4; 336 lines total).

## Current state (from `universe/last_scan.json` and `refresh_universe.py plan`)

- **State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- **Snapshot:** `mcap_snapshot_20261128_052955` (25/25 pages, 2500 entries, lowest rank 2500 / $1,337,581, `coverage_reaches_below_floor=true`)
- **Expansion floor:** `SHR/USDT` $1,353,111
- **Universe:** 282 symbols (BTC/USDT ... SHR/USDT)
- **Grid:** 18,612 / 18,612 cells complete (282 × 66), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`
- **Fixtures:** 284 CSV files in `data/fixtures/` (incl. `SHR_USDT.csv`, 22,099 rows; 66 SHR grid cells)
- **Eligible unseen below floor:** 0 (`eligible_unseen_below_floor_count=0`, `batch_selected=[]`)
- **Next eligible refresh (24 h bound):** `2026-11-29T05:29:55.373985+00:00` (~15h42m47s from generation)
- **`results/FINAL_DECISION.md`** preserved; git tree clean

## Your single measurable task (offline first)

1. **Offline first — never guess:** recompute eligibility from `next_eligible_refresh_at` (`2026-11-29T05:29:55.373985+00:00`) with `PYTHONPATH=. python3 scripts/refresh_universe.py plan` (or `scripts/refresh_gate.py:gate_status(state)`) vs independent UTC (`date -u`, `datetime.now(timezone.utc)`). Confirm `refresh_allowed_now=false` / `eligible=false` before doing anything else.
2. **If NOT eligible (expected until 2026-11-29T05:29:55Z):** make **no provider calls**. Append exactly **one** gate-check row to `NEXT_AGENT_TASK.md` §4 (the table at the end of the file), refresh the handoff time/state in this file, `TASK_FOR_NEXT_AGENT.md` and the `NEXT_AGENT_TASK.md` header, then stop. Do not schedule wakeups. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply); each activation records exactly one row and nothing else.
3. **If eligible (`refresh_allowed_now=true`):** run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; provider calls allowed only after the bound). Record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, new bound.
4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): apply it through the repo's own cycle — `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market cap; acceptance is `completed_cells == universe_n * 66`. Requires pandas installed.
5. **Never:** rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow the AGENTS.md adaptive gate policy.

## Validation commands for the next agent

```bash
# 1. Check gate status (offline, stdlib-only if pandas missing)
PYTHONPATH=. python3 scripts/refresh_universe.py plan

# 2. Verify universe/grid integrity (requires pandas)
PYTHONPATH=. python3 -c "
import json
ranking = json.load(open('universe/mcap_rank.json'))
print(f'Universe N: {len(ranking[\"symbols\"])}')
print(f'Last symbol: {ranking[\"symbols\"][-1]}')
"
# Grid verification
PYTHONPATH=. python3 -c "
import json
progress = json.load(open('results/20261019_135940_grid/progress.json'))
print(f'Completed cells: {progress[\"completed_cells\"]}')
print(f'Symbols: {progress[\"n_symbols\"]}')
print(f'All processed: {progress[\"all_symbols_processed\"]}')
"
```

## Environment note

This session verified `python 3.12.3` + `requests 2.31.0` + `pandas 3.1.1` / `numpy 2.5.5` importable; `pytest` was NOT importable this session (`ModuleNotFoundError`, temp home partially wiped — only pytest missing). The temp home may be wiped between sessions — re-verify at the start of the next session; if missing, reinstall (`pip install --user pandas numpy pytest`) before any grid/signal/pytest work. Gate tooling (`refresh_gate.py`) is stdlib-only and runs without pandas.