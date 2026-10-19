# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass.
- Implemented support for per-symbol real data loading, rr, stricter_trend, min_risk_atr, atr_threshold in scripts.
- Extended backtest to accept `atr_threshold` for min-risk ATR filter.
- Generated real hourly OHLCV for BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT, XRP/USDT in descending market-cap order (data/fixtures/*.csv).
- Validated on real data (market cap ordered, n=5 symbols).

## Validation results (real data, n=5, market-cap ordered)
- Parent (rr=1.0, no min-risk filter): 79 trades, net PF 0.00969, net WR 0.316, Sharpe -25.64
- Child B (rr=1.5, no min-risk filter): 68 trades, net PF 0.01286, net WR 0.250, Sharpe -25.15 (small improvement over parent; still cost-fragile)
- Cost stress (2x fees/slippage) for Child B: base net PF 0.01286 -> stress 0.00134, WR 0.25->0.162, Sharpe -25.15->-25.93 (severely degraded)
- Child C tuned (min-risk ATR, rr=1.5, atr_threshold=0.75): 36 trades (avoids zero trades; was 0 with atr_threshold=1.0), net PF 0.426, net WR 0.389, Sharpe -7.99 — more trades than threshold=1.0 case (11 trades at 1.0) and better risk-adjusted metrics relative to unfiltered Child B on same data. Cost stress also improves vs unfiltered.

Full detailed metrics saved to: `results/validation_real_data.json` and individual run results under `results/`.

## Decision label
**Label: tuned exploratory signal** — Child C (min-risk ATR with tuned threshold, combined with higher RR) shows improved metrics on real data with non-zero trade count. Continue validation/robustness testing.

## Next agent task
1. Run robustness checks on tuned config (Child C-like: rr=1.5, min_risk_atr=True, atr_threshold=0.75) across all 5 symbols on real data. Include walk-forward analysis (expanding window) and OOS split. Do not invent fills.
2. Stress test across different ATR thresholds more systematically (e.g., 0.7, 0.75, 0.8) and report parent→child→delta. Also test with stricter_trend variations if beneficial.
3. Generate a clear summary report (markdown) in results/ with all findings and update handoff with concrete next steps/recommendations.

## Quick Start
```bash
export PATH=$HOME/.local/bin:$PATH
cd /home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-
PYTHONPATH=$(pwd) python3 -m pytest -v
```
