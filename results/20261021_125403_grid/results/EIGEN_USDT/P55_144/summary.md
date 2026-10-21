# EMA Hourly Continuation — EIGEN/USDT P55_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7947 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -1.3578 |
| sortino_ratio | -0.3599 |
| max_drawdown | 0.3334 |
| cagr | -0.1542 |
| net_avg_win | 82.1857 |
| net_avg_loss | -97.7070 |
| avg_hold_time_bars | 13.8582 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
