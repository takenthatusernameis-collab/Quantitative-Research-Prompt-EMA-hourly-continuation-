# NEXT AGENT TASK

## Status (Updated)
COMPLETED: Robustness pass — annualized hourly Sharpe/Sortino/CAGR, data validation (NaNs/dups/OHLC), config/default.json, same-bar conflict documented.

COMPLETED: Next Agent Task items 1–5 (this cycle):
1. tests/test_robustness.py — same-bar SL/TP conflict (long+short), risk=0/pathological skip, missing data/NaNs/dups handling
2. scripts/run_baseline.py — --config CLI override with validation; CLI args override config file values
3. metrics/metrics.py — exposure (bar-based) + avg_hold_time_bars (bar-based) added to calculate_metrics; backtest/backtest.py tracks exit_bar_index per Trade
4. backtest/walkforward.py — oos_split() and walk_forward_splits() (expanding window, no leakage)
5. scripts/cost_stress.py — 1x vs 2x fees/slippage comparison with delta metrics

All 16 tests pass (`PYTHONPATH=$(pwd) python3 -m pytest -v`). All modified files compile.

## Key finding (cost stress)
Baseline on fixture (N=3, 10bps+2bps): 15 trades, net win rate 1.00, net PF inf. At 2x cost (20bps+5bps): net win rate 0.00, net PF 0.0, Sharpe -6.25 → -21.24. Strategy is cost-fragile on this fixture — treat as **exploratory signal**, not a credible candidate, until validated on real market-cap-ordered crypto data.

## Next Agent Task (suggested focus)
Per PROMPT.md §3.4 decision labels and §5 useful extensions:
1. Assign a decision label (credible candidate / exploratory signal / rejected / blocked) with justification, ideally after running on real hourly OHLCV for top-N market-cap crypto in descending order.
2. If fragile: test controlled mutations from PROMPT.md §5 — e.g. ATR-based min risk filter (skip tiny EMA100 distances), stricter trend (close also above/below EMA100), alternate RR (1.5R). Record parent config → child config → delta metrics.
3. Obtain/fix real hourly OHLCV data for top market-cap symbols if data is a blocker (see PROMPT.md §5.4).

## Quick Start
```bash
export PATH=$HOME/.local/bin:$PATH
cd /home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-
PYTHONPATH=$(pwd) python3 -m pytest -v
PYTHONPATH=$(pwd) python3 scripts/run_baseline.py --fixture data/fixtures/sample_hourly.csv --mcap universe/mcap_rank.json --n 3
PYTHONPATH=$(pwd) python3 scripts/cost_stress.py --fixture data/fixtures/sample_hourly.csv --mcap universe/mcap_rank.json --n 3
```
EOF
