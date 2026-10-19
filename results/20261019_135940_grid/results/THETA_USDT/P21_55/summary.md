# EMA Hourly Continuation — THETA/USDT P21_55

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.4977 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -6.9645 |
| sortino_ratio | -2.9958 |
| max_drawdown | 0.9743 |
| cagr | -0.7638 |
| net_avg_win | 23.3526 |
| net_avg_loss | -37.9214 |
| avg_hold_time_bars | 4.9913 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
