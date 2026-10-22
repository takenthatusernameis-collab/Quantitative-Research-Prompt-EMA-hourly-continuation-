# EMA Hourly Continuation — IOTA/USDT P21_50

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.5103 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.9842 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -7.5265 |
| sortino_ratio | -3.3351 |
| max_drawdown | 0.9840 |
| cagr | -0.8062 |
| net_avg_win | 23.0385 |
| net_avg_loss | -36.9978 |
| avg_hold_time_bars | 4.6791 |
| exposure | 0.2101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
