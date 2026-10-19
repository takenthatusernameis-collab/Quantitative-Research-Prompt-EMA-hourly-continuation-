# EMA Hourly Continuation — IOTA/USDT P20_200

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7267 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 1.0026 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.8906 |
| sortino_ratio | -0.4984 |
| max_drawdown | 0.4620 |
| cagr | -0.2092 |
| net_avg_win | 69.2534 |
| net_avg_loss | -92.5875 |
| avg_hold_time_bars | 40.6888 |
| exposure | 0.6418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
