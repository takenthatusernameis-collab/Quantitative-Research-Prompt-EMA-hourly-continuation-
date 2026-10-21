# EMA Hourly Continuation — EIGEN/USDT P8_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.8547 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -0.8258 |
| sortino_ratio | -0.2000 |
| max_drawdown | 0.2502 |
| cagr | -0.0899 |
| net_avg_win | 89.8541 |
| net_avg_loss | -100.7537 |
| avg_hold_time_bars | 60.8468 |
| exposure | 0.7957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
