# EMA Hourly Continuation — BONK/USDT P20_50

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.5290 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8804 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -6.3075 |
| sortino_ratio | -2.7623 |
| max_drawdown | 0.9700 |
| cagr | -0.7475 |
| net_avg_win | 23.9009 |
| net_avg_loss | -38.8645 |
| avg_hold_time_bars | 4.6677 |
| exposure | 0.2088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
