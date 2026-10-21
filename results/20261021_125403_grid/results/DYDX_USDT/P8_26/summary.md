# EMA Hourly Continuation — DYDX/USDT P8_26

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.7149 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -3.0345 |
| sortino_ratio | -1.1490 |
| max_drawdown | 0.7329 |
| cagr | -0.4089 |
| net_avg_win | 54.5304 |
| net_avg_loss | -70.4277 |
| avg_hold_time_bars | 6.5940 |
| exposure | 0.2104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
