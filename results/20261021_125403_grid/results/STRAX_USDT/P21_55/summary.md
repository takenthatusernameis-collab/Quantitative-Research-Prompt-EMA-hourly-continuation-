# EMA Hourly Continuation — STRAX/USDT P21_55

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.6110 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.8729 |
| sortino_ratio | -1.3098 |
| max_drawdown | 0.7845 |
| cagr | -0.4552 |
| net_avg_win | 47.1422 |
| net_avg_loss | -66.4290 |
| avg_hold_time_bars | 10.0160 |
| exposure | 0.2574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
