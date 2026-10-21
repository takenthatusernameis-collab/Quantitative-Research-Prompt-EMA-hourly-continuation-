# EMA Hourly Continuation — PROM/USDT P34_200

**Symbol:** PROM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.6436 |
| gross_win_rate | 0.3900 |
| sharpe_ratio | -4.1380 |
| sortino_ratio | -1.0747 |
| max_drawdown | 0.7245 |
| cagr | -0.3961 |
| net_avg_win | 52.6588 |
| net_avg_loss | -67.6225 |
| avg_hold_time_bars | 29.8710 |
| exposure | 0.4630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
