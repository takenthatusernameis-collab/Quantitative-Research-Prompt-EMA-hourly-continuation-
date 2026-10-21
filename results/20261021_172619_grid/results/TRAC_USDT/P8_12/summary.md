# EMA Hourly Continuation — TRAC/USDT P8_12

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7471 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0601 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.7519 |
| sortino_ratio | -0.4626 |
| max_drawdown | 0.4772 |
| cagr | -0.1895 |
| net_avg_win | 70.4126 |
| net_avg_loss | -98.2447 |
| avg_hold_time_bars | 6.4243 |
| exposure | 0.0984 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
