# EMA Hourly Continuation — LQTY/USDT P89_100

**Symbol:** LQTY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.5071 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.7394 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -2.6224 |
| sortino_ratio | -0.4824 |
| max_drawdown | 0.4348 |
| cagr | -0.1987 |
| net_avg_win | 61.1677 |
| net_avg_loss | -91.4270 |
| avg_hold_time_bars | 4.9940 |
| exposure | 0.0377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
