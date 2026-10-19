# NEXT AGENT TASK

## Prior cycle — COMPLETED (verified)
- All 16 tests pass.
- Mutations run on fixture (N=3, parent: ema_fast=50, ema_slow=100, rr=1.0, 10bps+2bps).
- Parent: 15 trades, net win rate 1.00, net PF inf, Sharpe -6.25. At 2x cost: win rate 0.00, PF 0.0, Sharpe -21.24.
- Child A (stricter trend, close above EMA100): same as parent — no improvement.
- Child B (RR 1.5R): 1x Sharpe +5.66, win rate 1.00; 2x win rate 0.20, PF 0.11, Sharpe -16.53. Promising (Sharpe>0 at 1x, win rate>0 at 2x) but cost-fragile.
- Child C (ATR min-risk filter): 0 trades — filter too aggressive.

## Decision label
**Label: exploratory signal** — Child B promoted as candidate for validation; others discarded.

## Next agent task
Validate Child B (rr=1.5) on real market-cap-ordered crypto data (BTC/USDT, ETH/USDT, ...) in descending market-cap order; obtain/fix real hourly OHLCV. Do not invent fills. Also tune min-risk filter threshold (Child C) to avoid zero trades. Record parent→child→delta metrics.

## Quick Start
```bash
export PATH=$HOME/.local/bin:$PATH
cd /home/runner/work/Quantitative-Research-Prompt-EMA-hourly-continuation-/Quantitative-Research-Prompt-EMA-hourly-continuation-
PYTHONPATH=$(pwd) python3 -m pytest -v
```
