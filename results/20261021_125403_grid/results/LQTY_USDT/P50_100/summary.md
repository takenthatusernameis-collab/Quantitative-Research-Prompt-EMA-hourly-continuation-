# EMA Hourly Continuation — LQTY/USDT P50_100

**Symbol:** LQTY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8239 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -2.8472 |
| sortino_ratio | -0.8196 |
| max_drawdown | 0.6200 |
| cagr | -0.3136 |
| net_avg_win | 55.4217 |
| net_avg_loss | -74.2101 |
| avg_hold_time_bars | 8.7640 |
| exposure | 0.1630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
