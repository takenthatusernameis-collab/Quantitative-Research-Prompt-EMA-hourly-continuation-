# EMA Hourly Continuation — FLIP/USDT P34_100

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.5034 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -4.9897 |
| sortino_ratio | -1.4505 |
| max_drawdown | 0.8424 |
| cagr | -0.5134 |
| net_avg_win | 45.3202 |
| net_avg_loss | -68.4404 |
| avg_hold_time_bars | 14.5958 |
| exposure | 0.2873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
