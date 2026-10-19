# EMA Hourly Continuation — EIGEN/USDT P21_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.8522 |
| sortino_ratio | -1.0614 |
| max_drawdown | 0.6499 |
| cagr | -0.3957 |
| net_avg_win | 58.4066 |
| net_avg_loss | -81.6609 |
| avg_hold_time_bars | 12.0018 |
| exposure | 0.3780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
