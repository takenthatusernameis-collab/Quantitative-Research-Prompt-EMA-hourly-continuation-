# EMA Hourly Continuation — ONDO/USDT P8_50

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.8543 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0497 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -1.2525 |
| sortino_ratio | -0.4617 |
| max_drawdown | 0.4552 |
| cagr | -0.1943 |
| net_avg_win | 72.6339 |
| net_avg_loss | -89.8078 |
| avg_hold_time_bars | 13.0866 |
| exposure | 0.3914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
