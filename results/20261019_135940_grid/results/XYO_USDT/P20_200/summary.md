# EMA Hourly Continuation — XYO/USDT P20_200

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5310 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8086 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.3707 |
| sortino_ratio | -1.3391 |
| max_drawdown | 0.8128 |
| cagr | -0.4729 |
| net_avg_win | 43.3974 |
| net_avg_loss | -63.7380 |
| avg_hold_time_bars | 28.9057 |
| exposure | 0.6239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
