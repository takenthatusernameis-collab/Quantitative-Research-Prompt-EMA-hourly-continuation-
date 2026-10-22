# EMA Hourly Continuation — PIXEL/USDT P12_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.6327 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9646 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -4.9378 |
| sortino_ratio | -2.2057 |
| max_drawdown | 0.9340 |
| cagr | -0.6532 |
| net_avg_win | 33.4068 |
| net_avg_loss | -47.4607 |
| avg_hold_time_bars | 8.8245 |
| exposure | 0.4049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
