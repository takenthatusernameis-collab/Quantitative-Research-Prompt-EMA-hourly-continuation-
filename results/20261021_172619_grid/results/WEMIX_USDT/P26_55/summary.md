# EMA Hourly Continuation — WEMIX/USDT P26_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5602 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.7571 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -3.6113 |
| sortino_ratio | -0.9306 |
| max_drawdown | 0.6633 |
| cagr | -0.3495 |
| net_avg_win | 60.9526 |
| net_avg_loss | -78.6104 |
| avg_hold_time_bars | 11.6991 |
| exposure | 0.1750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
