# EMA Hourly Continuation — LSK/USDT P26_100

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7415 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9886 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.1602 |
| sortino_ratio | -0.6738 |
| max_drawdown | 0.5929 |
| cagr | -0.2702 |
| net_avg_win | 66.1663 |
| net_avg_loss | -87.0298 |
| avg_hold_time_bars | 15.6438 |
| exposure | 0.3413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
