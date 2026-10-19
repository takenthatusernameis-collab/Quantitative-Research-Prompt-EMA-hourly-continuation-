# EMA Hourly Continuation — NEAR/USDT P26_50

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.4694 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -7.5685 |
| sortino_ratio | -3.3222 |
| max_drawdown | 0.9839 |
| cagr | -0.8063 |
| net_avg_win | 19.9157 |
| net_avg_loss | -34.5916 |
| avg_hold_time_bars | 3.3751 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
