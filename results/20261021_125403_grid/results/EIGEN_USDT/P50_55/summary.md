# EMA Hourly Continuation — EIGEN/USDT P50_55

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 86 |
| net_profit_factor | 0.8493 |
| net_win_rate | 0.5233 |
| gross_profit_factor | 1.0898 |
| gross_win_rate | 0.5233 |
| sharpe_ratio | -0.5062 |
| sortino_ratio | -0.0749 |
| max_drawdown | 0.1088 |
| cagr | -0.0344 |
| net_avg_win | 86.7012 |
| net_avg_loss | -112.0411 |
| avg_hold_time_bars | 5.6163 |
| exposure | 0.0269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
