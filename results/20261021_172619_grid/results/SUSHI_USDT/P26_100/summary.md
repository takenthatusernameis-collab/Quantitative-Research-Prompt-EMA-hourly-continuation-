# EMA Hourly Continuation — SUSHI/USDT P26_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7761 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9724 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.7539 |
| sortino_ratio | -0.5445 |
| max_drawdown | 0.5064 |
| cagr | -0.2220 |
| net_avg_win | 69.8098 |
| net_avg_loss | -87.3211 |
| avg_hold_time_bars | 16.3214 |
| exposure | 0.3493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
