# EMA Hourly Continuation — EIGEN/USDT P8_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8135 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.2284 |
| sortino_ratio | -0.3395 |
| max_drawdown | 0.3351 |
| cagr | -0.1489 |
| net_avg_win | 78.1960 |
| net_avg_loss | -98.6416 |
| avg_hold_time_bars | 46.5161 |
| exposure | 0.8024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
