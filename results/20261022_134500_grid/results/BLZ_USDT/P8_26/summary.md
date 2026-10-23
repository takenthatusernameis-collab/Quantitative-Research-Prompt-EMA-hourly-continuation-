# EMA Hourly Continuation — BLZ/USDT P8_26

**Symbol:** BLZ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1529 |
| net_profit_factor | 0.4491 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.8856 |
| gross_win_rate | 0.4258 |
| sharpe_ratio | -11.3808 |
| sortino_ratio | -6.2437 |
| max_drawdown | 0.9996 |
| cagr | -0.9551 |
| net_avg_win | 13.1014 |
| net_avg_loss | -20.0056 |
| avg_hold_time_bars | 4.4572 |
| exposure | 0.3084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
