# EMA Hourly Continuation — CGPT/USDT P50_55

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.1542 |
| net_win_rate | 0.3283 |
| gross_profit_factor | 0.5316 |
| gross_win_rate | 0.3912 |
| sharpe_ratio | -12.3363 |
| sortino_ratio | -5.0890 |
| max_drawdown | 0.9990 |
| cagr | -0.9357 |
| net_avg_win | 6.9773 |
| net_avg_loss | -22.1178 |
| avg_hold_time_bars | 2.0403 |
| exposure | 0.0737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
