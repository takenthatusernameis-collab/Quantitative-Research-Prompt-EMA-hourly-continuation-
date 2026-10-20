# EMA Hourly Continuation — PHA/USDT P20_100

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5407 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7863 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -4.5742 |
| sortino_ratio | -1.6650 |
| max_drawdown | 0.8732 |
| cagr | -0.5532 |
| net_avg_win | 34.1642 |
| net_avg_loss | -49.8486 |
| avg_hold_time_bars | 13.7581 |
| exposure | 0.4240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
