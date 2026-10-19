# EMA Hourly Continuation — ZBCN/USDT P26_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7707 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.9267 |
| sortino_ratio | -0.6033 |
| max_drawdown | 0.5339 |
| cagr | -0.2565 |
| net_avg_win | 69.1729 |
| net_avg_loss | -93.0773 |
| avg_hold_time_bars | 22.5556 |
| exposure | 0.5166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
