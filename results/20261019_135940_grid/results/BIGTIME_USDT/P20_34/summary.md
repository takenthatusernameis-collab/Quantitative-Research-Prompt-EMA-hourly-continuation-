# EMA Hourly Continuation — BIGTIME/USDT P20_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.4585 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.8598 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -8.4245 |
| sortino_ratio | -3.9648 |
| max_drawdown | 0.9926 |
| cagr | -0.8558 |
| net_avg_win | 16.9096 |
| net_avg_loss | -29.8509 |
| avg_hold_time_bars | 3.2817 |
| exposure | 0.1650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
