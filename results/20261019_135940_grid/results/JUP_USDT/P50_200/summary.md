# EMA Hourly Continuation — JUP/USDT P50_200

**Symbol:** JUP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.5425 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.7939 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -3.7979 |
| sortino_ratio | -1.0947 |
| max_drawdown | 0.7475 |
| cagr | -0.4119 |
| net_avg_win | 45.9544 |
| net_avg_loss | -67.9099 |
| avg_hold_time_bars | 17.3279 |
| exposure | 0.3363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
