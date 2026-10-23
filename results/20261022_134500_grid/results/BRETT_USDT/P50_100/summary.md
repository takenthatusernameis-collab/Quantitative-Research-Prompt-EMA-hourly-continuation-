# EMA Hourly Continuation — BRETT/USDT P50_100

**Symbol:** BRETT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.6017 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8893 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -3.8549 |
| sortino_ratio | -1.3139 |
| max_drawdown | 0.7787 |
| cagr | -0.4705 |
| net_avg_win | 44.5684 |
| net_avg_loss | -66.0581 |
| avg_hold_time_bars | 6.9518 |
| exposure | 0.1873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
