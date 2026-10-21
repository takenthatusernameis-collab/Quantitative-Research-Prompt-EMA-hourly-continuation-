# EMA Hourly Continuation — EIGEN/USDT P26_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.9089 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0508 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -0.5253 |
| sortino_ratio | -0.1437 |
| max_drawdown | 0.1940 |
| cagr | -0.0681 |
| net_avg_win | 88.3368 |
| net_avg_loss | -102.5932 |
| avg_hold_time_bars | 27.0473 |
| exposure | 0.4455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
