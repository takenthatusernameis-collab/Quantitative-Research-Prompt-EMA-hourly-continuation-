# EMA Hourly Continuation — EIGEN/USDT P89_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.7165 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8485 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -1.7873 |
| sortino_ratio | -0.4412 |
| max_drawdown | 0.3691 |
| cagr | -0.1842 |
| net_avg_win | 75.6607 |
| net_avg_loss | -90.5172 |
| avg_hold_time_bars | 12.1417 |
| exposure | 0.1669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
