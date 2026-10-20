# EMA Hourly Continuation — AIOZ/USDT P8_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1243 |
| net_profit_factor | 0.6486 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -6.2664 |
| sortino_ratio | -3.1015 |
| max_drawdown | 0.9777 |
| cagr | -0.7755 |
| net_avg_win | 31.2362 |
| net_avg_loss | -41.7244 |
| avg_hold_time_bars | 7.9043 |
| exposure | 0.4466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
