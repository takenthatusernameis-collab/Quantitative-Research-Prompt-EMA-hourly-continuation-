# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass: `PYTHONPATH=$(pwd) python3 -m pytest -v`
- Robustness pass: annualized hourly Sharpe/Sortino/CAGR, data validation (NaNs/dups/OHLC), config/default.json, same-bar conflict documented.
- Items 1–5 done: tests/test_robustness.py, scripts/run_baseline.py (--config CLI override), metrics/metrics.py (exposure + avg_hold_time_bars), backtest/walkforward.py (oos_split/walk_forward_splits), scripts/cost_stress.py (1x vs 2x).
- All modified files compile.

## Decision label (this cycle)
**Label: exploratory signal** — not a credible candidate yet.
Justification (fixture N=3, baseline 10bps+2bps per side): 15 trades, net win rate 1.00, net PF inf, Sharpe -6.25. At 2x cost (20bps+5bps): net win rate 0.00, net PF 0.0, Sharpe -21.24. Edge vanishes under modest cost stress → cost-fragile, treat as exploratory signal until validated on real market-cap-ordered crypto data (see `results/20261019_005703_cost_stress/`).

## Next agent task (narrow, per PROMPT.md §3.4 / §5 / §6)
Run controlled mutations on the fixture and record parent config → child config → delta metrics:
1. Child A: stricter trend — require close also above EMA100 (long) / below EMA100 (short) at entry.
2. Child B: alternate RR 1.5R (TP = entry + 1.5*risk; SL unchanged at 1*risk).
3. Child C: ATR-based min risk filter — skip trades where risk < ATR-based floor.
4. Baseline parent config: ema_fast=50, ema_slow=100, rr=1.0, taker=10bps, slippage=2bps, no min-risk filter.

For each child: run baseline cost + 2x cost stress, report net Sharpe / net PF / net win rate / trade count vs parent. Acceptance: any child with net Sharpe > 0 at 1x cost AND net win rate > 0 at 2x cost on the fixture is worth promoting; otherwise keep label "exploratory signal" and escalate to the data blocker.

Data blocker (if mutations fail): obtain/fix real hourly OHLCV for top-N market-cap crypto (BTC/USDT, ETH/USDT, ...) in descending market-cap order; do not invent fills (PROMPT.md §6.5).

## Quick Start
```bash
export PATH=$HOME/.local/bin:$PATH
cd /home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-
PYTHONPATH=$(pwd) python3 -m pytest -v
PYTHONPATH=$(pwd) python3 scripts/run_baseline.py --fixture data/fixtures/sample_hourly.csv --mcap universe/mcap_rank.json --n 3
PYTHONPATH=$(pwd) python3 scripts/cost_stress.py --fixture data/fixtures/sample_hourly.csv --mcap universe/mcap_rank.json --n 3
```
EOF
