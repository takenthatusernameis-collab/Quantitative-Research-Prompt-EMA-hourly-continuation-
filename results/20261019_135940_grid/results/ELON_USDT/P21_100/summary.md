# EMA Hourly Continuation — ELON/USDT P21_100

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.5043 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8018 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -5.7631 |
| sortino_ratio | -2.1840 |
| max_drawdown | 0.9341 |
| cagr | -0.6537 |
| net_avg_win | 29.6715 |
| net_avg_loss | -45.6642 |
| avg_hold_time_bars | 10.8123 |
| exposure | 0.3588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
