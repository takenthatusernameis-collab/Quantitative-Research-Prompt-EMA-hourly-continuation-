# EMA Hourly Continuation — VR/USDT P26_89

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.5743 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.7294 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -3.2381 |
| sortino_ratio | -0.8703 |
| max_drawdown | 0.6446 |
| cagr | -0.3329 |
| net_avg_win | 55.5360 |
| net_avg_loss | -72.0670 |
| avg_hold_time_bars | 17.1047 |
| exposure | 0.2822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
