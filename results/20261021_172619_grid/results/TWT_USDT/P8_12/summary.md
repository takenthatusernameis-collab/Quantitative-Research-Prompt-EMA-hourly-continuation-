# EMA Hourly Continuation — TWT/USDT P8_12

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6324 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.0555 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -2.2352 |
| sortino_ratio | -0.5711 |
| max_drawdown | 0.5024 |
| cagr | -0.2268 |
| net_avg_win | 50.2066 |
| net_avg_loss | -87.4436 |
| avg_hold_time_bars | 4.4084 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
