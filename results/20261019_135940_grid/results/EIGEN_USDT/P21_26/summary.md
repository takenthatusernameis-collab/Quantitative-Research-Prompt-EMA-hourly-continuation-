# EMA Hourly Continuation — EIGEN/USDT P21_26

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.2974 |
| net_win_rate | 0.3914 |
| gross_profit_factor | 0.5983 |
| gross_win_rate | 0.4165 |
| sharpe_ratio | -12.0823 |
| sortino_ratio | -5.8818 |
| max_drawdown | 0.9983 |
| cagr | -0.9544 |
| net_avg_win | 11.2685 |
| net_avg_loss | -24.3703 |
| avg_hold_time_bars | 1.9509 |
| exposure | 0.1040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
