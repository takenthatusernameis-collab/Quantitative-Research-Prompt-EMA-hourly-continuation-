# EMA Hourly Continuation — IOTA/USDT P89_100

**Symbol:** IOTA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.4486 |
| net_win_rate | 0.3925 |
| gross_profit_factor | 0.6533 |
| gross_win_rate | 0.3925 |
| sharpe_ratio | -2.5540 |
| sortino_ratio | -0.3766 |
| max_drawdown | 0.3756 |
| cagr | -0.1604 |
| net_avg_win | 68.8399 |
| net_avg_loss | -99.1509 |
| avg_hold_time_bars | 5.4393 |
| exposure | 0.0265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
