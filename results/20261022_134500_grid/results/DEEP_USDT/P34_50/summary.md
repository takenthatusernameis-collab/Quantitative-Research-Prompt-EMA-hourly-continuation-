# EMA Hourly Continuation — DEEP/USDT P34_50

**Symbol:** DEEP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.5488 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9298 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -6.0898 |
| sortino_ratio | -2.4545 |
| max_drawdown | 0.9141 |
| cagr | -0.7004 |
| net_avg_win | 35.6731 |
| net_avg_loss | -58.7619 |
| avg_hold_time_bars | 2.9221 |
| exposure | 0.1084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
