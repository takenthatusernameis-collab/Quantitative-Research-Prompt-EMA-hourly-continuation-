# EMA Hourly Continuation — CYBER/USDT P144_200

**Symbol:** CYBER/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.4508 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7948 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -4.6061 |
| sortino_ratio | -1.2604 |
| max_drawdown | 0.7957 |
| cagr | -0.4687 |
| net_avg_win | 38.6490 |
| net_avg_loss | -68.3446 |
| avg_hold_time_bars | 5.6457 |
| exposure | 0.0978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
