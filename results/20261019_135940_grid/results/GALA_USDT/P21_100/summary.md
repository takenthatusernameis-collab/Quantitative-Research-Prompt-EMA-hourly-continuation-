# EMA Hourly Continuation — GALA/USDT P21_100

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.5756 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8125 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -4.1896 |
| sortino_ratio | -1.4578 |
| max_drawdown | 0.8273 |
| cagr | -0.4947 |
| net_avg_win | 40.7396 |
| net_avg_loss | -58.3715 |
| avg_hold_time_bars | 16.4371 |
| exposure | 0.4513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
