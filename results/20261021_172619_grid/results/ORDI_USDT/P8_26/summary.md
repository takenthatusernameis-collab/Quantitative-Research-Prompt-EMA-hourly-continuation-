# EMA Hourly Continuation — ORDI/USDT P8_26

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9739 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.3809 |
| sortino_ratio | -0.8709 |
| max_drawdown | 0.6449 |
| cagr | -0.3303 |
| net_avg_win | 63.1498 |
| net_avg_loss | -79.5041 |
| avg_hold_time_bars | 8.0642 |
| exposure | 0.2397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
