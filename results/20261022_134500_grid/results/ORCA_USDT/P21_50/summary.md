# EMA Hourly Continuation — ORCA/USDT P21_50

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.5530 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9440 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.9525 |
| sortino_ratio | -2.4824 |
| max_drawdown | 0.9565 |
| cagr | -0.7063 |
| net_avg_win | 28.3734 |
| net_avg_loss | -45.5062 |
| avg_hold_time_bars | 5.7390 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
