# EMA Hourly Continuation — FLR/USDT P26_50

**Symbol:** FLR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.5265 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.7718 |
| gross_win_rate | 0.4362 |
| sharpe_ratio | -4.2728 |
| sortino_ratio | -1.2671 |
| max_drawdown | 0.7899 |
| cagr | -0.4408 |
| net_avg_win | 45.6373 |
| net_avg_loss | -66.4371 |
| avg_hold_time_bars | 6.4339 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
