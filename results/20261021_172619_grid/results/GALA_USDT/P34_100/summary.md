# EMA Hourly Continuation — GALA/USDT P34_100

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7190 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.0967 |
| sortino_ratio | -0.6114 |
| max_drawdown | 0.5236 |
| cagr | -0.2453 |
| net_avg_win | 65.4963 |
| net_avg_loss | -81.6111 |
| avg_hold_time_bars | 14.0239 |
| exposure | 0.2671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
