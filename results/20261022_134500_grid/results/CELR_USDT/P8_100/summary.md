# EMA Hourly Continuation — CELR/USDT P8_100

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -3.5987 |
| sortino_ratio | -1.2728 |
| max_drawdown | 0.7810 |
| cagr | -0.4503 |
| net_avg_win | 46.0968 |
| net_avg_loss | -64.5623 |
| avg_hold_time_bars | 23.6035 |
| exposure | 0.6708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
