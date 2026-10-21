# EMA Hourly Continuation — PENDLE/USDT P26_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.8552 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1015 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -0.9667 |
| sortino_ratio | -0.2866 |
| max_drawdown | 0.3638 |
| cagr | -0.1254 |
| net_avg_win | 75.9936 |
| net_avg_loss | -98.6369 |
| avg_hold_time_bars | 6.7204 |
| exposure | 0.1289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
