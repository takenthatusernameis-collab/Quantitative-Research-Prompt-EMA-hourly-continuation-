# EMA Hourly Continuation — SHIB/USDT P21_34

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.2810 |
| net_win_rate | 0.3980 |
| gross_profit_factor | 0.7845 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -12.3607 |
| sortino_ratio | -5.8782 |
| max_drawdown | 0.9996 |
| cagr | -0.9555 |
| net_avg_win | 8.9810 |
| net_avg_loss | -21.1287 |
| avg_hold_time_bars | 2.3083 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
