# EMA Hourly Continuation — EGLD/USDT P55_100

**Symbol:** EGLD/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0436 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.6006 |
| sortino_ratio | -0.4427 |
| max_drawdown | 0.4200 |
| cagr | -0.1833 |
| net_avg_win | 63.5950 |
| net_avg_loss | -89.7764 |
| avg_hold_time_bars | 7.5393 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
