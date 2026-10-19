# EMA Hourly Continuation — EIGEN/USDT P20_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 805 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -5.5217 |
| sortino_ratio | -2.4451 |
| max_drawdown | 0.9096 |
| cagr | -0.6901 |
| net_avg_win | 33.7497 |
| net_avg_loss | -50.7824 |
| avg_hold_time_bars | 4.7590 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
