# EMA Hourly Continuation — ATOM/USDT P34_50

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.2720 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.7923 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -9.4092 |
| sortino_ratio | -3.9683 |
| max_drawdown | 0.9934 |
| cagr | -0.8630 |
| net_avg_win | 9.9509 |
| net_avg_loss | -28.0160 |
| avg_hold_time_bars | 2.6767 |
| exposure | 0.1046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
