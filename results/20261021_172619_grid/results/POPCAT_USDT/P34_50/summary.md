# EMA Hourly Continuation — POPCAT/USDT P34_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8658 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.6243 |
| sortino_ratio | -0.6551 |
| max_drawdown | 0.5252 |
| cagr | -0.2599 |
| net_avg_win | 72.0620 |
| net_avg_loss | -94.4102 |
| avg_hold_time_bars | 4.9508 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
