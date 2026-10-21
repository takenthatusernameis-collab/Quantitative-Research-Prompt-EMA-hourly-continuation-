# EMA Hourly Continuation — EGLD/USDT P8_12

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.6561 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 0.9893 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -2.3148 |
| sortino_ratio | -0.5671 |
| max_drawdown | 0.4970 |
| cagr | -0.2275 |
| net_avg_win | 63.6428 |
| net_avg_loss | -94.3582 |
| avg_hold_time_bars | 4.4724 |
| exposure | 0.0590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
