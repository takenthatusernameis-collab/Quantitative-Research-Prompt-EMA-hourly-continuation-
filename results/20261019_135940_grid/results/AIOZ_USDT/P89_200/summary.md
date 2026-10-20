# EMA Hourly Continuation — AIOZ/USDT P89_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6200 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8989 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -3.8193 |
| sortino_ratio | -1.1542 |
| max_drawdown | 0.7757 |
| cagr | -0.4239 |
| net_avg_win | 58.5290 |
| net_avg_loss | -79.2329 |
| avg_hold_time_bars | 8.9847 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
