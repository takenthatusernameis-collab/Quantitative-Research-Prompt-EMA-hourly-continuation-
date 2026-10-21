# EMA Hourly Continuation — CGPT/USDT P8_100

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.9170 |
| net_win_rate | 0.5240 |
| gross_profit_factor | 1.0930 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -0.5345 |
| sortino_ratio | -0.1648 |
| max_drawdown | 0.2542 |
| cagr | -0.0782 |
| net_avg_win | 85.1323 |
| net_avg_loss | -102.2058 |
| avg_hold_time_bars | 32.0175 |
| exposure | 0.6665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
