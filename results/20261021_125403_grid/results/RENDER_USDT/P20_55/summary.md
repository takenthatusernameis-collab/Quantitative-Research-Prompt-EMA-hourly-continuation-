# EMA Hourly Continuation — RENDER/USDT P20_55

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8595 |
| net_win_rate | 0.5297 |
| gross_profit_factor | 1.1074 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -0.9685 |
| sortino_ratio | -0.3087 |
| max_drawdown | 0.3318 |
| cagr | -0.1348 |
| net_avg_win | 73.7345 |
| net_avg_loss | -96.6199 |
| avg_hold_time_bars | 7.8504 |
| exposure | 0.1744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
