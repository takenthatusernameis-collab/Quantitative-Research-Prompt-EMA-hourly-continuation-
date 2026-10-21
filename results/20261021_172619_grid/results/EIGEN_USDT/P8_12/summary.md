# EMA Hourly Continuation — EIGEN/USDT P8_12

**Symbol:** EIGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.6540 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.0316 |
| sortino_ratio | -0.4512 |
| max_drawdown | 0.3517 |
| cagr | -0.1868 |
| net_avg_win | 71.0277 |
| net_avg_loss | -94.2574 |
| avg_hold_time_bars | 3.7828 |
| exposure | 0.0417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
