# EMA Hourly Continuation — PEPE/USDT P34_100

**Symbol:** PEPE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8253 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.1327 |
| sortino_ratio | -0.3051 |
| max_drawdown | 0.3282 |
| cagr | -0.1323 |
| net_avg_win | 79.5562 |
| net_avg_loss | -98.0452 |
| avg_hold_time_bars | 14.1813 |
| exposure | 0.2275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
