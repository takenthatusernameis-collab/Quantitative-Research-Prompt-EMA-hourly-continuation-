# EMA Hourly Continuation — CPOOL/USDT P12_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -5.9592 |
| sortino_ratio | -2.7455 |
| max_drawdown | 0.9674 |
| cagr | -0.7424 |
| net_avg_win | 29.6822 |
| net_avg_loss | -41.4118 |
| avg_hold_time_bars | 6.4977 |
| exposure | 0.3240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
