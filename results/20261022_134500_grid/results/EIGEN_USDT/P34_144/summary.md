# EMA Hourly Continuation — EIGEN/USDT P34_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7900 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0459 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.7725 |
| sortino_ratio | -0.5796 |
| max_drawdown | 0.4826 |
| cagr | -0.2387 |
| net_avg_win | 73.6062 |
| net_avg_loss | -96.2449 |
| avg_hold_time_bars | 16.3318 |
| exposure | 0.3917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
