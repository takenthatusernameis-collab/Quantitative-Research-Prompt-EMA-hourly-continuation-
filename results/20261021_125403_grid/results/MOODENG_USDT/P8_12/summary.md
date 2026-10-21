# EMA Hourly Continuation — MOODENG/USDT P8_12

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.5470 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.7534 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -3.0276 |
| sortino_ratio | -0.7133 |
| max_drawdown | 0.5084 |
| cagr | -0.2800 |
| net_avg_win | 60.6579 |
| net_avg_loss | -85.5697 |
| avg_hold_time_bars | 5.2178 |
| exposure | 0.0650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
