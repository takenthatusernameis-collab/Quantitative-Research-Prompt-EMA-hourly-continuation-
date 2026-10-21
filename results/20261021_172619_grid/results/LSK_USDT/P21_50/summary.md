# EMA Hourly Continuation — LSK/USDT P21_50

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.4453 |
| sortino_ratio | -1.1549 |
| max_drawdown | 0.7403 |
| cagr | -0.4097 |
| net_avg_win | 49.4798 |
| net_avg_loss | -70.3238 |
| avg_hold_time_bars | 8.1384 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
