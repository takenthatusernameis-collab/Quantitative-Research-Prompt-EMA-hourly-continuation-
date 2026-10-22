# EMA Hourly Continuation — KMNO/USDT P26_50

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.5391 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.9529 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -6.2437 |
| sortino_ratio | -2.5391 |
| max_drawdown | 0.9523 |
| cagr | -0.7073 |
| net_avg_win | 30.0106 |
| net_avg_loss | -46.7296 |
| avg_hold_time_bars | 4.2694 |
| exposure | 0.1603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
