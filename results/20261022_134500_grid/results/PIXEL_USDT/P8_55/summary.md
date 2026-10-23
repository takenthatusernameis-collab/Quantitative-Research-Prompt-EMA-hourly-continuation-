# EMA Hourly Continuation — PIXEL/USDT P8_55

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 1.0327 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -4.3116 |
| sortino_ratio | -1.9297 |
| max_drawdown | 0.9098 |
| cagr | -0.6017 |
| net_avg_win | 39.9080 |
| net_avg_loss | -54.9699 |
| avg_hold_time_bars | 11.0897 |
| exposure | 0.5093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
