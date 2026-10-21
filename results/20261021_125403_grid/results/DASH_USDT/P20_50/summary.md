# EMA Hourly Continuation — DASH/USDT P20_50

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6773 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -2.5339 |
| sortino_ratio | -0.7854 |
| max_drawdown | 0.5973 |
| cagr | -0.3013 |
| net_avg_win | 54.8813 |
| net_avg_loss | -76.0067 |
| avg_hold_time_bars | 8.0277 |
| exposure | 0.1711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
