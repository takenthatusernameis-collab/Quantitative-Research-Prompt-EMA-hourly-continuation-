# EMA Hourly Continuation — DOT/USDT P26_55

**Symbol:** DOT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8341 |
| net_win_rate | 0.5369 |
| gross_profit_factor | 1.1558 |
| gross_win_rate | 0.5369 |
| sharpe_ratio | -1.1098 |
| sortino_ratio | -0.3186 |
| max_drawdown | 0.3859 |
| cagr | -0.1365 |
| net_avg_win | 73.4327 |
| net_avg_loss | -102.0692 |
| avg_hold_time_bars | 7.3893 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
