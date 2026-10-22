# EMA Hourly Continuation — LTC/USDT P89_100

**Symbol:** LTC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.1096 |
| net_win_rate | 0.3097 |
| gross_profit_factor | 0.5262 |
| gross_win_rate | 0.3821 |
| sharpe_ratio | -12.6517 |
| sortino_ratio | -4.8912 |
| max_drawdown | 0.9989 |
| cagr | -0.9341 |
| net_avg_win | 6.2393 |
| net_avg_loss | -25.5542 |
| avg_hold_time_bars | 2.2374 |
| exposure | 0.0647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
