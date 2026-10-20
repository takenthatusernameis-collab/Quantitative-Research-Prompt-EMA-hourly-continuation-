# EMA Hourly Continuation — ROSE/USDT P20_100

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9322 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -3.9284 |
| sortino_ratio | -1.4412 |
| max_drawdown | 0.8341 |
| cagr | -0.4942 |
| net_avg_win | 50.2979 |
| net_avg_loss | -66.5430 |
| avg_hold_time_bars | 14.7360 |
| exposure | 0.4541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
