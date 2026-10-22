# EMA Hourly Continuation — OSMO/USDT P21_50

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6428 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -3.6687 |
| sortino_ratio | -1.1941 |
| max_drawdown | 0.7579 |
| cagr | -0.4229 |
| net_avg_win | 56.8524 |
| net_avg_loss | -73.8032 |
| avg_hold_time_bars | 8.2917 |
| exposure | 0.1964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
