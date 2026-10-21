# EMA Hourly Continuation — METIS/USDT P50_100

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.6422 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -2.7156 |
| sortino_ratio | -0.7391 |
| max_drawdown | 0.5877 |
| cagr | -0.2886 |
| net_avg_win | 62.1543 |
| net_avg_loss | -80.3258 |
| avg_hold_time_bars | 8.6612 |
| exposure | 0.1441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
