# EMA Hourly Continuation — AERO/USDT P50_100

**Symbol:** AERO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9393 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -1.6255 |
| sortino_ratio | -0.4192 |
| max_drawdown | 0.4030 |
| cagr | -0.1756 |
| net_avg_win | 73.7366 |
| net_avg_loss | -92.2239 |
| avg_hold_time_bars | 9.3313 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
