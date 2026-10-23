# EMA Hourly Continuation — SUSHI/USDT P21_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6093 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8723 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -3.0355 |
| sortino_ratio | -0.8911 |
| max_drawdown | 0.6667 |
| cagr | -0.3473 |
| net_avg_win | 50.1314 |
| net_avg_loss | -72.0851 |
| avg_hold_time_bars | 29.7267 |
| exposure | 0.5905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
