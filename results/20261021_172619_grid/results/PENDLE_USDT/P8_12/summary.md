# EMA Hourly Continuation — PENDLE/USDT P8_12

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -2.4453 |
| sortino_ratio | -0.5658 |
| max_drawdown | 0.4888 |
| cagr | -0.2286 |
| net_avg_win | 68.9008 |
| net_avg_loss | -89.5711 |
| avg_hold_time_bars | 5.2765 |
| exposure | 0.0633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
