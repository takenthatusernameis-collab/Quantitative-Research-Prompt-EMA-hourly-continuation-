# NEXT AGENT TASK

## Status (Updated)
COMPLETED: Robustness pass — annualized hourly Sharpe/Sortino/CAGR, data validation (NaNs/dups/OHLC), config/default.json, same-bar conflict documented.

## Implementation Summary
- metrics: hourly annualization (sqrt(24*365)) for Sharpe/Sortino; CAGR annualized by years
- data_loader: duplicate timestamp drop, numeric coercion, OHLC sanity filter
- config/default.json: EMA periods, costs, warmup, risk threshold
- Same-bar conflict rule: prioritize SL (adverse) — documented in backtest

## Next Agent Task
Focus on validation tests and extensibility:
1. Add tests: same-bar SL/TP conflict, risk=0/pathological, missing data/NaNs/dups
2. Add config override via CLI (--config) and validation
3. Add exposure + avg hold time (bar-based) metrics
4. Walk-forward / OOS split support
5. Cost stress test (2x fees/slippage) harness

## Quick Start
```bash
export PATH=$HOME/.local/bin:$PATH
cd /home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-
PYTHONPATH=$(pwd) python3 -m pytest -v
PYTHONPATH=$(pwd) python3 scripts/run_baseline.py --fixture data/fixtures/sample_hourly.csv --mcap universe/mcap_rank.json --n 3
```
EOF
echo done