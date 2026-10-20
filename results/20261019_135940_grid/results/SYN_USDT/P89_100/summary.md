# EMA Hourly Continuation — SYN/USDT P89_100

**Symbol:** SYN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.3321 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7770 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -7.6097 |
| sortino_ratio | -2.6483 |
| max_drawdown | 0.9660 |
| cagr | -0.7384 |
| net_avg_win | 19.5168 |
| net_avg_loss | -41.5417 |
| avg_hold_time_bars | 2.9310 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
