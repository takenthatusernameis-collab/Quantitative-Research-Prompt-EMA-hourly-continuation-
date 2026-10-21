# EMA Hourly Continuation — EIGEN/USDT P12_26

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7002 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8779 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.3969 |
| sortino_ratio | -0.7278 |
| max_drawdown | 0.5559 |
| cagr | -0.2846 |
| net_avg_win | 66.7026 |
| net_avg_loss | -84.1375 |
| avg_hold_time_bars | 5.2183 |
| exposure | 0.1077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
