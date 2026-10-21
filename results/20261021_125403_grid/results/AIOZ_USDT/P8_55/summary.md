# EMA Hourly Continuation — AIOZ/USDT P8_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.8390 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.5363 |
| sortino_ratio | -0.5755 |
| max_drawdown | 0.5667 |
| cagr | -0.2356 |
| net_avg_win | 74.3297 |
| net_avg_loss | -89.6339 |
| avg_hold_time_bars | 14.3904 |
| exposure | 0.4474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
