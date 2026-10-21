# EMA Hourly Continuation — PROM/USDT P55_100

**Symbol:** PROM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.2156 |
| sortino_ratio | -0.9068 |
| max_drawdown | 0.6736 |
| cagr | -0.3426 |
| net_avg_win | 48.4239 |
| net_avg_loss | -72.9763 |
| avg_hold_time_bars | 8.6760 |
| exposure | 0.1546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
