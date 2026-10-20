# EMA Hourly Continuation — CPOOL/USDT P26_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.5053 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.7824 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -6.6003 |
| sortino_ratio | -2.7768 |
| max_drawdown | 0.9706 |
| cagr | -0.7520 |
| net_avg_win | 24.0979 |
| net_avg_loss | -38.9714 |
| avg_hold_time_bars | 3.4508 |
| exposure | 0.1434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
