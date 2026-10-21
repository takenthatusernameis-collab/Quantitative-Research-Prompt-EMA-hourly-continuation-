# EMA Hourly Continuation — ATOM/USDT P21_200

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8722 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0680 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.6765 |
| sortino_ratio | -0.1697 |
| max_drawdown | 0.2440 |
| cagr | -0.0776 |
| net_avg_win | 79.2581 |
| net_avg_loss | -98.3424 |
| avg_hold_time_bars | 43.5362 |
| exposure | 0.6016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
