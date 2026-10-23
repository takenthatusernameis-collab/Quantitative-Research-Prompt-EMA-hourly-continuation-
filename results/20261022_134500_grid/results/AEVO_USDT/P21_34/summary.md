# EMA Hourly Continuation — AEVO/USDT P21_34

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.3534 |
| net_win_rate | 0.4102 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -10.2662 |
| sortino_ratio | -4.9069 |
| max_drawdown | 0.9979 |
| cagr | -0.9134 |
| net_avg_win | 11.6562 |
| net_avg_loss | -22.9334 |
| avg_hold_time_bars | 2.8405 |
| exposure | 0.1467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
