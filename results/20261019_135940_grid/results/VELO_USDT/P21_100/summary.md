# EMA Hourly Continuation — VELO/USDT P21_100

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.7372 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -2.6617 |
| sortino_ratio | -1.0180 |
| max_drawdown | 0.7486 |
| cagr | -0.3816 |
| net_avg_win | 53.8674 |
| net_avg_loss | -73.4722 |
| avg_hold_time_bars | 12.1140 |
| exposure | 0.4009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
