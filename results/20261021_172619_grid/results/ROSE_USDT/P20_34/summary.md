# EMA Hourly Continuation — ROSE/USDT P20_34

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8927 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.5479 |
| sortino_ratio | -0.6995 |
| max_drawdown | 0.5690 |
| cagr | -0.2730 |
| net_avg_win | 59.5418 |
| net_avg_loss | -81.3819 |
| avg_hold_time_bars | 5.0461 |
| exposure | 0.0846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
