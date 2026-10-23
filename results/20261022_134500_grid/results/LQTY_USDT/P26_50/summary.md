# EMA Hourly Continuation — LQTY/USDT P26_50

**Symbol:** LQTY/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.4542 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8418 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -7.1690 |
| sortino_ratio | -3.1477 |
| max_drawdown | 0.9789 |
| cagr | -0.7806 |
| net_avg_win | 18.5860 |
| net_avg_loss | -34.1387 |
| avg_hold_time_bars | 4.1651 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
