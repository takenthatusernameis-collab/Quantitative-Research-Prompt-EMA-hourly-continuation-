# EMA Hourly Continuation — MAGIC/USDT P26_50

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9623 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -6.2005 |
| sortino_ratio | -2.6299 |
| max_drawdown | 0.9609 |
| cagr | -0.7195 |
| net_avg_win | 29.1816 |
| net_avg_loss | -45.9464 |
| avg_hold_time_bars | 4.6508 |
| exposure | 0.1907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
