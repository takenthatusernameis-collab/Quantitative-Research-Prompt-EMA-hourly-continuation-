# EMA Hourly Continuation — CRO/USDT P12_100

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7377 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9913 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.9499 |
| sortino_ratio | -0.6089 |
| max_drawdown | 0.5363 |
| cagr | -0.2444 |
| net_avg_win | 59.4665 |
| net_avg_loss | -81.6328 |
| avg_hold_time_bars | 25.5916 |
| exposure | 0.5525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
