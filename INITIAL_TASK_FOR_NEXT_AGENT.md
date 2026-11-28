# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Generated:** 2026-11-28T21:31:09Z

## Current State Summary

- **Gate status:** NOT ELIGIBLE (24 h refresh bound has not elapsed)
- **Bound:** `2026-11-29T05:29:55.373985+00:00` (~7h58m45s / 28,725s remaining)
- **State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- **Last snapshot:** `mcap_snapshot_20261128_052955` (25/25 pages, 2500 entries, lowest rank 2500 / $1,337,581, `coverage_reaches_below_floor=true`)
- **Expansion floor:** `SHR/USDT` $1,353,111
- **Eligible unseen below floor:** 0
- **Universe:** 282 symbols (BTC/USDT through SHR/USDT)
- **Grid:** 18,612 completed cells (282 × 66 pairs), all symbols processed
- **Fixtures:** 284 CSV files in `data/fixtures/` (including `SHR_USDT.csv` with 22,099 rows)
- **Environment:** python 3.12.3 + requests 2.31.0 only — pandas/numpy/pytest NOT importable (temp home wiped); gate tooling stdlib-only
- **Git tree:** clean

## Your Task (One Measurable Task)

1. **Offline first:** Read `NEXT_AGENT_TASK.md` and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` (`2026-11-29T05:29:55.373985+00:00`) with `scripts/refresh_gate.py:gate_status` vs independent UTC (`date -u`, `datetime.now(timezone.utc)`); never guess.

2. **If NOT eligible (expected until 2026-11-29T05:29:55Z):** Make **no provider calls**. Append exactly one gate-check row to the log table in `NEXT_AGENT_TASK.md` (following the existing format), then stop. Do not schedule wakeups. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply); each activation records exactly one row and nothing else.

3. **If eligible:** Run **exactly one** pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10` (no `--apply`; provider calls allowed only after the bound). Record snapshot id, coverage (must reach below the floor), floor, `eligible_unseen_below_floor_count`, new bound.

4. **If that pass yields a batch** (`EXPANSION_AVAILABLE`): Apply it through the repo's own cycle — `refresh_universe.py fetch` (or `fetch_mcap_snapshot.py --apply`), then `fixtures`, `grid`, `state`, `log` — new symbols only, full 66-pair grid, ascending compute but descending market cap; acceptance is `completed_cells == universe_n * 66`. Requires pandas installed.

5. **Never:** Rerun existing grid cells, re-fetch a fixture the grid already used, fetch candles unnecessarily, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow the AGENTS.md adaptive gate policy.

## Validation Commands for Next Agent

```bash
# 1. Check gate status (stdlib-only, works without pandas/numpy/pytest)
python3 -c "
import json
from scripts.refresh_gate import gate_status
with open('universe/last_scan.json') as f:
    state = json.load(f)
result = gate_status(state)
print(json.dumps(result, indent=2))
"

# 2. Verify universe/grid state (requires pandas - install if needed)
# pip install --user pandas numpy pytest
# PYTHONPATH=. python3 scripts/refresh_universe.py plan

# 3. Quick offline verification
python3 -c "
import json
with open('universe/last_scan.json') as f:
    s = json.load(f)
print('State:', s['state'])
print('Snapshot:', s['snapshot_id'])
print('Universe n:', s['universe_n'])
print('Floor:', s['expansion_floor'])
print('Eligible unseen:', s['eligible_unseen_below_floor_count'])
print('Next refresh:', s['next_eligible_refresh_at'])
"

# 4. Verify grid completion
python3 -c "
import json
with open('results/20261019_135940_grid/progress.json') as f:
    d = json.load(f)
print('n_symbols:', d['n_symbols'])
print('n_pairs:', d['n_pairs'])
print('completed_cells:', d['completed_cells'])
print('Expected:', d['n_symbols'] * d['n_pairs'])
print('Match:', d['completed_cells'] == d['n_symbols'] * d['n_pairs'])
"
```

## Expected Outcome

- One new row appended to the gate-check log table in `NEXT_AGENT_TASK.md`
- Updated header timestamp in `NEXT_AGENT_TASK.md`
- No provider calls, no file modifications other than the handoff log
- Clean stop until the next activation after the bound elapses