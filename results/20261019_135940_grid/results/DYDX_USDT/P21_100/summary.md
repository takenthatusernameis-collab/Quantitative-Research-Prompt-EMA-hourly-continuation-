# EMA Hourly Continuation — DYDX/USDT P21_100

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6809 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -3.0415 |
| sortino_ratio | -1.0777 |
| max_drawdown | 0.7305 |
| cagr | -0.3998 |
| net_avg_win | 49.5705 |
| net_avg_loss | -70.3147 |
| avg_hold_time_bars | 15.6082 |
| exposure | 0.4491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
