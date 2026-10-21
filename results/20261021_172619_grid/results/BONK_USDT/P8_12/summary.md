# EMA Hourly Continuation — BONK/USDT P8_12

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9516 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -1.6001 |
| sortino_ratio | -0.3311 |
| max_drawdown | 0.3595 |
| cagr | -0.1409 |
| net_avg_win | 79.6664 |
| net_avg_loss | -103.8642 |
| avg_hold_time_bars | 4.4067 |
| exposure | 0.0419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
