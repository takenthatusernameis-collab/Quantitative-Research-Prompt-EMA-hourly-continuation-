# EMA Hourly Continuation — EIGEN/USDT P26_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8441 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9693 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -0.9402 |
| sortino_ratio | -0.2434 |
| max_drawdown | 0.2679 |
| cagr | -0.1080 |
| net_avg_win | 85.7337 |
| net_avg_loss | -98.5848 |
| avg_hold_time_bars | 34.2164 |
| exposure | 0.5103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
