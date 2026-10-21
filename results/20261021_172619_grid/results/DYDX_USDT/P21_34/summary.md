# EMA Hourly Continuation — DYDX/USDT P21_34

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.7315 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0144 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.8470 |
| sortino_ratio | -0.4738 |
| max_drawdown | 0.4436 |
| cagr | -0.1938 |
| net_avg_win | 71.6148 |
| net_avg_loss | -97.2852 |
| avg_hold_time_bars | 4.8621 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
