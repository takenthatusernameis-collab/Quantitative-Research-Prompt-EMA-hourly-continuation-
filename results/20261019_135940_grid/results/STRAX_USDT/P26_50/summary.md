# EMA Hourly Continuation — STRAX/USDT P26_50

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.4869 |
| net_win_rate | 0.4218 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -8.7406 |
| sortino_ratio | -3.8096 |
| max_drawdown | 0.9919 |
| cagr | -0.8539 |
| net_avg_win | 23.4096 |
| net_avg_loss | -35.0790 |
| avg_hold_time_bars | 5.4092 |
| exposure | 0.2357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
