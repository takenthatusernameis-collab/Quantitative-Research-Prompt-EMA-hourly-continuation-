# EMA Hourly Continuation — LUNA/USDT P12_100

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.4431 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4269 |
| sharpe_ratio | -7.2453 |
| sortino_ratio | -2.8284 |
| max_drawdown | 0.9726 |
| cagr | -0.7601 |
| net_avg_win | 23.8011 |
| net_avg_loss | -38.3691 |
| avg_hold_time_bars | 15.3410 |
| exposure | 0.5439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
