# EMA Hourly Continuation — CHZ/USDT P21_55

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.5229 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.9299 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -7.1914 |
| sortino_ratio | -3.1053 |
| max_drawdown | 0.9787 |
| cagr | -0.7833 |
| net_avg_win | 25.4134 |
| net_avg_loss | -39.5174 |
| avg_hold_time_bars | 5.2455 |
| exposure | 0.2244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
