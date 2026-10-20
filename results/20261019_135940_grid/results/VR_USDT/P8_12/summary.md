# EMA Hourly Continuation — VR/USDT P8_12

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1905 |
| net_profit_factor | 0.2323 |
| net_win_rate | 0.2278 |
| gross_profit_factor | 0.5599 |
| gross_win_rate | 0.2667 |
| sharpe_ratio | -25.7398 |
| sortino_ratio | -17.3873 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 6.9729 |
| net_avg_loss | -8.8554 |
| avg_hold_time_bars | 2.2525 |
| exposure | 0.1950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
