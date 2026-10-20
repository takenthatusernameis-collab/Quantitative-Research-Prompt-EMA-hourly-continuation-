# EMA Hourly Continuation — DYDX/USDT P20_50

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 997 |
| net_profit_factor | 0.5277 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.9278 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -7.2791 |
| sortino_ratio | -3.2172 |
| max_drawdown | 0.9821 |
| cagr | -0.7952 |
| net_avg_win | 24.6946 |
| net_avg_loss | -37.5732 |
| avg_hold_time_bars | 4.8375 |
| exposure | 0.2192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
