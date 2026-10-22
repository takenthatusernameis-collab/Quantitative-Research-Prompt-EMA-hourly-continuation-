# EMA Hourly Continuation — DOGS/USDT P21_50

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.6379 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.7971 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -2.7589 |
| sortino_ratio | -0.8186 |
| max_drawdown | 0.5545 |
| cagr | -0.3132 |
| net_avg_win | 57.8044 |
| net_avg_loss | -74.7006 |
| avg_hold_time_bars | 6.7941 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
