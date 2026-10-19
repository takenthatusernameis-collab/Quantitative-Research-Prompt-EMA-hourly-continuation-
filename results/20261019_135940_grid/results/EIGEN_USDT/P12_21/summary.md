# EMA Hourly Continuation — EIGEN/USDT P12_21

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1194 |
| net_profit_factor | 0.4327 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.7943 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -10.9969 |
| sortino_ratio | -5.9234 |
| max_drawdown | 0.9978 |
| cagr | -0.9491 |
| net_avg_win | 15.2536 |
| net_avg_loss | -25.3083 |
| avg_hold_time_bars | 2.1868 |
| exposure | 0.1453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
