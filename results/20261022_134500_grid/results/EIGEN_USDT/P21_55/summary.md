# EMA Hourly Continuation — EIGEN/USDT P21_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -5.1152 |
| sortino_ratio | -2.2302 |
| max_drawdown | 0.8854 |
| cagr | -0.6521 |
| net_avg_win | 35.0106 |
| net_avg_loss | -52.2097 |
| avg_hold_time_bars | 5.0077 |
| exposure | 0.2162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
