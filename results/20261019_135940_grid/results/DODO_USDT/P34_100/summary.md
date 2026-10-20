# EMA Hourly Continuation — DODO/USDT P34_100

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.5899 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.9087 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -5.2667 |
| sortino_ratio | -2.0130 |
| max_drawdown | 0.9145 |
| cagr | -0.6161 |
| net_avg_win | 39.3369 |
| net_avg_loss | -54.8290 |
| avg_hold_time_bars | 7.9133 |
| exposure | 0.2643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
