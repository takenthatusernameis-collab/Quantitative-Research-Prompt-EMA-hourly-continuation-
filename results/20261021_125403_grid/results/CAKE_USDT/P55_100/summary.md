# EMA Hourly Continuation — CAKE/USDT P55_100

**Symbol:** CAKE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9471 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.3845 |
| sortino_ratio | -0.6182 |
| max_drawdown | 0.5281 |
| cagr | -0.2465 |
| net_avg_win | 59.4216 |
| net_avg_loss | -87.3894 |
| avg_hold_time_bars | 9.1865 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
