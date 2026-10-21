# EMA Hourly Continuation — PHA/USDT P26_200

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7350 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8616 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -1.7671 |
| sortino_ratio | -0.4644 |
| max_drawdown | 0.4582 |
| cagr | -0.1933 |
| net_avg_win | 72.7400 |
| net_avg_loss | -85.5180 |
| avg_hold_time_bars | 33.2449 |
| exposure | 0.5183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
