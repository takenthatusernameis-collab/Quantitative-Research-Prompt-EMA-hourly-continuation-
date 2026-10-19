# EMA Hourly Continuation — DOGE/USDT P50_100

**Symbol:** DOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.4661 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8348 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -6.1428 |
| sortino_ratio | -2.1466 |
| max_drawdown | 0.9346 |
| cagr | -0.6609 |
| net_avg_win | 29.3236 |
| net_avg_loss | -51.1414 |
| avg_hold_time_bars | 6.2935 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
