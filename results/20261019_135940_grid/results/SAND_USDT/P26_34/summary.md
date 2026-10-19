# EMA Hourly Continuation — SAND/USDT P26_34

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.2581 |
| net_win_rate | 0.3666 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -13.1695 |
| sortino_ratio | -6.1062 |
| max_drawdown | 0.9997 |
| cagr | -0.9613 |
| net_avg_win | 9.2728 |
| net_avg_loss | -20.7939 |
| avg_hold_time_bars | 2.0381 |
| exposure | 0.0948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
