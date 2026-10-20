# EMA Hourly Continuation — DYDX/USDT P89_100

**Symbol:** DYDX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.3615 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.9612 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -7.8630 |
| sortino_ratio | -2.7720 |
| max_drawdown | 0.9736 |
| cagr | -0.7613 |
| net_avg_win | 20.7794 |
| net_avg_loss | -44.1530 |
| avg_hold_time_bars | 2.2869 |
| exposure | 0.0634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
