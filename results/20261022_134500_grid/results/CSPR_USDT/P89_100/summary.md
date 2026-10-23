# EMA Hourly Continuation — CSPR/USDT P89_100

**Symbol:** CSPR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.1737 |
| net_win_rate | 0.3358 |
| gross_profit_factor | 0.5379 |
| gross_win_rate | 0.3604 |
| sharpe_ratio | -12.3708 |
| sortino_ratio | -5.1550 |
| max_drawdown | 0.9991 |
| cagr | -0.9381 |
| net_avg_win | 7.6942 |
| net_avg_loss | -22.3912 |
| avg_hold_time_bars | 2.3702 |
| exposure | 0.0876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
