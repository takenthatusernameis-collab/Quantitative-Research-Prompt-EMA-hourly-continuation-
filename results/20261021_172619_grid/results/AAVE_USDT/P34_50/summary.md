# EMA Hourly Continuation — AAVE/USDT P34_50

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0077 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5526 |
| sortino_ratio | -0.3366 |
| max_drawdown | 0.3518 |
| cagr | -0.1427 |
| net_avg_win | 74.1934 |
| net_avg_loss | -102.3310 |
| avg_hold_time_bars | 5.0658 |
| exposure | 0.0525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
