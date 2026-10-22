# EMA Hourly Continuation — EIGEN/USDT P12_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7474 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 1.0026 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -2.7095 |
| sortino_ratio | -1.0076 |
| max_drawdown | 0.6663 |
| cagr | -0.3803 |
| net_avg_win | 66.3100 |
| net_avg_loss | -85.3570 |
| avg_hold_time_bars | 16.9473 |
| exposure | 0.5366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
