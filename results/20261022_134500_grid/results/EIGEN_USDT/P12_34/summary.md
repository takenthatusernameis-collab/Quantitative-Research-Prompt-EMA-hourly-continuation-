# EMA Hourly Continuation — EIGEN/USDT P12_34

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.5633 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -6.9344 |
| sortino_ratio | -3.4824 |
| max_drawdown | 0.9708 |
| cagr | -0.8176 |
| net_avg_win | 26.0576 |
| net_avg_loss | -39.0895 |
| avg_hold_time_bars | 3.7624 |
| exposure | 0.2194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
