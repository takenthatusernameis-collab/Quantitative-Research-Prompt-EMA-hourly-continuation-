# EMA Hourly Continuation — CWEB/USDT P8_100

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5776 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8856 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -4.8681 |
| sortino_ratio | -1.5377 |
| max_drawdown | 0.8648 |
| cagr | -0.5405 |
| net_avg_win | 52.6126 |
| net_avg_loss | -68.6282 |
| avg_hold_time_bars | 29.5838 |
| exposure | 0.6979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
