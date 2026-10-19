# EMA Hourly Continuation — EIGEN/USDT P8_50

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.6389 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -4.6912 |
| sortino_ratio | -2.1234 |
| max_drawdown | 0.8822 |
| cagr | -0.6417 |
| net_avg_win | 38.1787 |
| net_avg_loss | -54.1671 |
| avg_hold_time_bars | 9.8271 |
| exposure | 0.4681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
