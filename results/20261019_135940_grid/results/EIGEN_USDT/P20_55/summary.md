# EMA Hourly Continuation — EIGEN/USDT P20_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.6023 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9074 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -5.0160 |
| sortino_ratio | -2.1939 |
| max_drawdown | 0.8833 |
| cagr | -0.6490 |
| net_avg_win | 36.0511 |
| net_avg_loss | -53.5120 |
| avg_hold_time_bars | 5.2532 |
| exposure | 0.2298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
