# EMA Hourly Continuation — PUNDIX/USDT P8_21

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.5481 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8302 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -5.6263 |
| sortino_ratio | -2.1932 |
| max_drawdown | 0.9249 |
| cagr | -0.6359 |
| net_avg_win | 33.8530 |
| net_avg_loss | -49.5884 |
| avg_hold_time_bars | 6.3549 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
