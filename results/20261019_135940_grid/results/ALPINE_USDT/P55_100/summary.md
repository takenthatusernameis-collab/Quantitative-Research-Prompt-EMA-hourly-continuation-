# EMA Hourly Continuation — ALPINE/USDT P55_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.4505 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.8102 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -6.8820 |
| sortino_ratio | -2.4341 |
| max_drawdown | 0.9533 |
| cagr | -0.7011 |
| net_avg_win | 29.5565 |
| net_avg_loss | -47.3257 |
| avg_hold_time_bars | 6.5619 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
