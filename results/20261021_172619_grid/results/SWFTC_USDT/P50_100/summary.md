# EMA Hourly Continuation — SWFTC/USDT P50_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7639 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9832 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.4452 |
| sortino_ratio | -0.3432 |
| max_drawdown | 0.3381 |
| cagr | -0.1462 |
| net_avg_win | 77.9724 |
| net_avg_loss | -99.8623 |
| avg_hold_time_bars | 9.2873 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
