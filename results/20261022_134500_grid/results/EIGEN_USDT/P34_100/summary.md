# EMA Hourly Continuation — EIGEN/USDT P34_100

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.6437 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9053 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -3.7777 |
| sortino_ratio | -1.3689 |
| max_drawdown | 0.7426 |
| cagr | -0.4812 |
| net_avg_win | 52.0107 |
| net_avg_loss | -72.3510 |
| avg_hold_time_bars | 8.6287 |
| exposure | 0.2612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
