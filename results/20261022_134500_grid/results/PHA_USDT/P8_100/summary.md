# EMA Hourly Continuation — PHA/USDT P8_100

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -3.7944 |
| sortino_ratio | -1.4218 |
| max_drawdown | 0.8267 |
| cagr | -0.4916 |
| net_avg_win | 43.1141 |
| net_avg_loss | -59.0577 |
| avg_hold_time_bars | 19.9339 |
| exposure | 0.6442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
