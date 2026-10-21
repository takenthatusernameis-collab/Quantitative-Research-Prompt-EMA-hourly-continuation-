# EMA Hourly Continuation — ORCA/USDT P26_50

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0740 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -2.1521 |
| sortino_ratio | -0.6877 |
| max_drawdown | 0.5860 |
| cagr | -0.2718 |
| net_avg_win | 65.5891 |
| net_avg_loss | -92.5648 |
| avg_hold_time_bars | 7.1455 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
