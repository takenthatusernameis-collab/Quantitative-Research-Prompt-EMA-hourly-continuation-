# EMA Hourly Continuation — EIGEN/USDT P21_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8099 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0729 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -1.4294 |
| sortino_ratio | -0.4498 |
| max_drawdown | 0.3754 |
| cagr | -0.1909 |
| net_avg_win | 73.6269 |
| net_avg_loss | -95.5897 |
| avg_hold_time_bars | 23.8191 |
| exposure | 0.5275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
