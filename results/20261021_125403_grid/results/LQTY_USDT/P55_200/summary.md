# EMA Hourly Continuation — LQTY/USDT P55_200

**Symbol:** LQTY/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8355 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -1.9728 |
| sortino_ratio | -0.4789 |
| max_drawdown | 0.4389 |
| cagr | -0.1977 |
| net_avg_win | 68.1180 |
| net_avg_loss | -84.6477 |
| avg_hold_time_bars | 27.1361 |
| exposure | 0.3610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
