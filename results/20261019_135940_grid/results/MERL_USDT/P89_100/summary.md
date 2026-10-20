# EMA Hourly Continuation — MERL/USDT P89_100

**Symbol:** MERL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.3582 |
| net_win_rate | 0.3913 |
| gross_profit_factor | 0.6926 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -8.0418 |
| sortino_ratio | -2.8045 |
| max_drawdown | 0.9740 |
| cagr | -0.7576 |
| net_avg_win | 23.1663 |
| net_avg_loss | -41.5751 |
| avg_hold_time_bars | 2.2609 |
| exposure | 0.0616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
