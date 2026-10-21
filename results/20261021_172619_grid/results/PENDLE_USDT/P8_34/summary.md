# EMA Hourly Continuation — PENDLE/USDT P8_34

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.7560 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9477 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.4306 |
| sortino_ratio | -0.9334 |
| max_drawdown | 0.7077 |
| cagr | -0.3486 |
| net_avg_win | 58.0092 |
| net_avg_loss | -72.8062 |
| avg_hold_time_bars | 9.1466 |
| exposure | 0.3006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
