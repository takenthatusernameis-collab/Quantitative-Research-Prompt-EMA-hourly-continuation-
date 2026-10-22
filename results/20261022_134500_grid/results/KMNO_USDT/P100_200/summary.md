# EMA Hourly Continuation — KMNO/USDT P100_200

**Symbol:** KMNO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6665 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9668 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.4090 |
| sortino_ratio | -0.6486 |
| max_drawdown | 0.5463 |
| cagr | -0.2648 |
| net_avg_win | 60.1354 |
| net_avg_loss | -88.7189 |
| avg_hold_time_bars | 10.3501 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
