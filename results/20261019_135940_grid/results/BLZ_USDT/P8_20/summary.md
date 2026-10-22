# EMA Hourly Continuation — BLZ/USDT P8_20

**Symbol:** BLZ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1630 |
| net_profit_factor | 0.4313 |
| net_win_rate | 0.3847 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4160 |
| sharpe_ratio | -13.4554 |
| sortino_ratio | -7.6746 |
| max_drawdown | 0.9999 |
| cagr | -0.9789 |
| net_avg_win | 12.0927 |
| net_avg_loss | -17.5289 |
| avg_hold_time_bars | 3.6098 |
| exposure | 0.2663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
