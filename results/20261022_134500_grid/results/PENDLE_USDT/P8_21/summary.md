# EMA Hourly Continuation — PENDLE/USDT P8_21

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1628 |
| net_profit_factor | 0.4636 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8817 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -10.3979 |
| sortino_ratio | -5.9188 |
| max_drawdown | 0.9993 |
| cagr | -0.9456 |
| net_avg_win | 12.1290 |
| net_avg_loss | -20.3375 |
| avg_hold_time_bars | 3.0559 |
| exposure | 0.2261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
