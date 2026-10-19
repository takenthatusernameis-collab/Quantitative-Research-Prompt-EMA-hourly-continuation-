# EMA Hourly Continuation — ALGO/USDT P26_100

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0530 |
| gross_win_rate | 0.5180 |
| sharpe_ratio | -3.2034 |
| sortino_ratio | -1.1611 |
| max_drawdown | 0.7708 |
| cagr | -0.4277 |
| net_avg_win | 42.7691 |
| net_avg_loss | -66.3874 |
| avg_hold_time_bars | 10.7132 |
| exposure | 0.3243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
