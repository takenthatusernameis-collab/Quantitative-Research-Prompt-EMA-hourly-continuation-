# EMA Hourly Continuation — BRETT/USDT P8_50

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.8290 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9751 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.4967 |
| sortino_ratio | -0.5665 |
| max_drawdown | 0.4849 |
| cagr | -0.2331 |
| net_avg_win | 68.8493 |
| net_avg_loss | -82.0506 |
| avg_hold_time_bars | 12.8807 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
