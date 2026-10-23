# EMA Hourly Continuation — ORDI/USDT P50_100

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0621 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -3.3305 |
| sortino_ratio | -1.1821 |
| max_drawdown | 0.7540 |
| cagr | -0.4243 |
| net_avg_win | 48.6978 |
| net_avg_loss | -73.3672 |
| avg_hold_time_bars | 6.3355 |
| exposure | 0.1794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
