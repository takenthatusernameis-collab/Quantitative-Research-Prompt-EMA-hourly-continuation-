# EMA Hourly Continuation — PHA/USDT P20_26

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.7809 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0610 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.2086 |
| sortino_ratio | -0.2573 |
| max_drawdown | 0.3332 |
| cagr | -0.1118 |
| net_avg_win | 81.9451 |
| net_avg_loss | -109.8427 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
