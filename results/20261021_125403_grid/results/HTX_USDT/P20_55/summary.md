# EMA Hourly Continuation — HTX/USDT P20_55

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.4156 |
| net_win_rate | 0.4007 |
| gross_profit_factor | 0.7191 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -7.0008 |
| sortino_ratio | -2.3582 |
| max_drawdown | 0.9392 |
| cagr | -0.6704 |
| net_avg_win | 30.6372 |
| net_avg_loss | -49.2962 |
| avg_hold_time_bars | 10.2739 |
| exposure | 0.2529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
