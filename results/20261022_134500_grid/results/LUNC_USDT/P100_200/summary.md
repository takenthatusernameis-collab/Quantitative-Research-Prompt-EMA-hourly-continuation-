# EMA Hourly Continuation — LUNC/USDT P100_200

**Symbol:** LUNC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5127 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.8642 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -4.3032 |
| sortino_ratio | -1.2912 |
| max_drawdown | 0.7940 |
| cagr | -0.4595 |
| net_avg_win | 40.7663 |
| net_avg_loss | -66.4292 |
| avg_hold_time_bars | 9.5336 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
