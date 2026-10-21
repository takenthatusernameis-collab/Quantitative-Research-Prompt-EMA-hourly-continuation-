# EMA Hourly Continuation — PHA/USDT P20_55

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.8200 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0333 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.4967 |
| sortino_ratio | -0.4978 |
| max_drawdown | 0.5003 |
| cagr | -0.2057 |
| net_avg_win | 73.5414 |
| net_avg_loss | -92.0542 |
| avg_hold_time_bars | 8.7002 |
| exposure | 0.2124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
