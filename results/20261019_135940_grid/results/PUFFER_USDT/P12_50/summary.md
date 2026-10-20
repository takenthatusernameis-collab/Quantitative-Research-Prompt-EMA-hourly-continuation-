# EMA Hourly Continuation — PUFFER/USDT P12_50

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 789 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.5006 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -3.7486 |
| sortino_ratio | -1.6623 |
| max_drawdown | 0.7990 |
| cagr | -0.5449 |
| net_avg_win | 43.0519 |
| net_avg_loss | -63.3558 |
| avg_hold_time_bars | 8.0925 |
| exposure | 0.3613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
