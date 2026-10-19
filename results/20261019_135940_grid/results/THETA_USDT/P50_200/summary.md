# EMA Hourly Continuation — THETA/USDT P50_200

**Symbol:** THETA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6663 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.1070 |
| sortino_ratio | -0.5626 |
| max_drawdown | 0.5024 |
| cagr | -0.2337 |
| net_avg_win | 55.6188 |
| net_avg_loss | -80.7086 |
| avg_hold_time_bars | 25.1376 |
| exposure | 0.4068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
