# EMA Hourly Continuation — JASMY/USDT P8_100

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.9599 |
| net_win_rate | 0.5352 |
| gross_profit_factor | 1.1392 |
| gross_win_rate | 0.5352 |
| sharpe_ratio | -0.2070 |
| sortino_ratio | -0.0648 |
| max_drawdown | 0.2186 |
| cagr | -0.0369 |
| net_avg_win | 86.0281 |
| net_avg_loss | -103.1850 |
| avg_hold_time_bars | 30.6610 |
| exposure | 0.6536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
