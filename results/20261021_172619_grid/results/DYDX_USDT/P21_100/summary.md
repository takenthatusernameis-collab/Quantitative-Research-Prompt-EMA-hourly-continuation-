# EMA Hourly Continuation — DYDX/USDT P21_100

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -1.3697 |
| sortino_ratio | -0.4127 |
| max_drawdown | 0.4174 |
| cagr | -0.1742 |
| net_avg_win | 69.8724 |
| net_avg_loss | -86.3553 |
| avg_hold_time_bars | 21.5856 |
| exposure | 0.4356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
