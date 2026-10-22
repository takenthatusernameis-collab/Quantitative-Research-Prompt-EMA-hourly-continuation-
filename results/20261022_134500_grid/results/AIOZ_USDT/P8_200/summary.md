# EMA Hourly Continuation — AIOZ/USDT P8_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6776 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -3.1453 |
| sortino_ratio | -1.0310 |
| max_drawdown | 0.7393 |
| cagr | -0.3833 |
| net_avg_win | 58.8774 |
| net_avg_loss | -76.7897 |
| avg_hold_time_bars | 31.2617 |
| exposure | 0.7602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
