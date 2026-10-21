# EMA Hourly Continuation — EIGEN/USDT P34_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8800 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0166 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -0.7391 |
| sortino_ratio | -0.2034 |
| max_drawdown | 0.2478 |
| cagr | -0.0926 |
| net_avg_win | 87.2083 |
| net_avg_loss | -101.0924 |
| avg_hold_time_bars | 22.7409 |
| exposure | 0.3809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
