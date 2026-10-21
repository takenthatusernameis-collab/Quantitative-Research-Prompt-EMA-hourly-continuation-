# EMA Hourly Continuation — ANKR/USDT P21_34

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4855 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.7463 |
| gross_win_rate | 0.4293 |
| sharpe_ratio | -4.6218 |
| sortino_ratio | -1.3517 |
| max_drawdown | 0.7934 |
| cagr | -0.4645 |
| net_avg_win | 41.7379 |
| net_avg_loss | -64.6523 |
| avg_hold_time_bars | 8.0480 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
