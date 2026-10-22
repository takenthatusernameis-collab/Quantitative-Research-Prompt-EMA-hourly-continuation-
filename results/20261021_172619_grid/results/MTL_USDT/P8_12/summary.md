# EMA Hourly Continuation — MTL/USDT P8_12

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.4836 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -6.2443 |
| sortino_ratio | -2.1453 |
| max_drawdown | 0.9255 |
| cagr | -0.6389 |
| net_avg_win | 34.8627 |
| net_avg_loss | -54.8464 |
| avg_hold_time_bars | 4.8380 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
