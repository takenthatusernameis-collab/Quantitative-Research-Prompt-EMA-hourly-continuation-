# EMA Hourly Continuation — ANYONE/USDT P8_12

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.6842 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.3612 |
| sortino_ratio | -0.6335 |
| max_drawdown | 0.5459 |
| cagr | -0.2531 |
| net_avg_win | 69.7441 |
| net_avg_loss | -90.4695 |
| avg_hold_time_bars | 5.3793 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
