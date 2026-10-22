# EMA Hourly Continuation — BTC/USDT P34_200

**Symbol:** BTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5032 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -4.3264 |
| sortino_ratio | -1.1521 |
| max_drawdown | 0.8073 |
| cagr | -0.4384 |
| net_avg_win | 43.5032 |
| net_avg_loss | -72.2300 |
| avg_hold_time_bars | 29.1114 |
| exposure | 0.4809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
