# EMA Hourly Continuation — ALPINE/USDT P50_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4815 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.8504 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -6.5642 |
| sortino_ratio | -2.3355 |
| max_drawdown | 0.9476 |
| cagr | -0.6871 |
| net_avg_win | 31.9426 |
| net_avg_loss | -49.7101 |
| avg_hold_time_bars | 7.0981 |
| exposure | 0.2071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
