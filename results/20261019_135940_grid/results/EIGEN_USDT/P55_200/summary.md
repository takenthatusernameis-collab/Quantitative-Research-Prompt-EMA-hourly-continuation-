# EMA Hourly Continuation — EIGEN/USDT P55_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6920 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.6713 |
| sortino_ratio | -0.7782 |
| max_drawdown | 0.5668 |
| cagr | -0.3121 |
| net_avg_win | 72.5228 |
| net_avg_loss | -93.5284 |
| avg_hold_time_bars | 18.9233 |
| exposure | 0.3707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
