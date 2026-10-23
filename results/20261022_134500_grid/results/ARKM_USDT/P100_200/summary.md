# EMA Hourly Continuation — ARKM/USDT P100_200

**Symbol:** ARKM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8066 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -3.7504 |
| sortino_ratio | -1.0995 |
| max_drawdown | 0.7347 |
| cagr | -0.4062 |
| net_avg_win | 47.1720 |
| net_avg_loss | -68.1512 |
| avg_hold_time_bars | 8.6528 |
| exposure | 0.1699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
