# EMA Hourly Continuation — CVX/USDT P8_26

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.7598 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0055 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -2.3649 |
| sortino_ratio | -0.9319 |
| max_drawdown | 0.6669 |
| cagr | -0.3476 |
| net_avg_win | 54.9165 |
| net_avg_loss | -73.0439 |
| avg_hold_time_bars | 6.7281 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
