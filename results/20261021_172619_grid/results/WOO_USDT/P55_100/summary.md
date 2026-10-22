# EMA Hourly Continuation — WOO/USDT P55_100

**Symbol:** WOO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7018 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9297 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.3139 |
| sortino_ratio | -0.6317 |
| max_drawdown | 0.5495 |
| cagr | -0.2525 |
| net_avg_win | 70.1125 |
| net_avg_loss | -90.5412 |
| avg_hold_time_bars | 8.5464 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
