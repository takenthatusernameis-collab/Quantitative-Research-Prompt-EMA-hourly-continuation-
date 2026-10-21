# EMA Hourly Continuation — PHA/USDT P89_200

**Symbol:** PHA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9143 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -1.4508 |
| sortino_ratio | -0.3480 |
| max_drawdown | 0.3617 |
| cagr | -0.1487 |
| net_avg_win | 73.8334 |
| net_avg_loss | -90.9287 |
| avg_hold_time_bars | 13.3958 |
| exposure | 0.1723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
