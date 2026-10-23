# EMA Hourly Continuation — PIXEL/USDT P89_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -2.5383 |
| sortino_ratio | -0.6637 |
| max_drawdown | 0.5473 |
| cagr | -0.2655 |
| net_avg_win | 64.8044 |
| net_avg_loss | -83.8828 |
| avg_hold_time_bars | 14.5249 |
| exposure | 0.2241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
