# EMA Hourly Continuation — TRAC/USDT P50_100

**Symbol:** TRAC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7637 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 0.9986 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.5564 |
| sortino_ratio | -0.4290 |
| max_drawdown | 0.4063 |
| cagr | -0.1783 |
| net_avg_win | 68.0043 |
| net_avg_loss | -89.5315 |
| avg_hold_time_bars | 7.9919 |
| exposure | 0.1340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
