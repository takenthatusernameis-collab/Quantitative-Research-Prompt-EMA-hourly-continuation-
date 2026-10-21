# EMA Hourly Continuation — SUSHI/USDT P26_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6877 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.5958 |
| sortino_ratio | -0.7689 |
| max_drawdown | 0.6061 |
| cagr | -0.2966 |
| net_avg_win | 62.8869 |
| net_avg_loss | -83.7251 |
| avg_hold_time_bars | 6.4965 |
| exposure | 0.1267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
