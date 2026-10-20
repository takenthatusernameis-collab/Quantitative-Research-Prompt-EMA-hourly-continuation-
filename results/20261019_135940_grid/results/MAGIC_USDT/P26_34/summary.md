# EMA Hourly Continuation — MAGIC/USDT P26_34

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.3694 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4584 |
| sharpe_ratio | -10.2732 |
| sortino_ratio | -4.6993 |
| max_drawdown | 0.9976 |
| cagr | -0.9092 |
| net_avg_win | 13.4364 |
| net_avg_loss | -26.4117 |
| avg_hold_time_bars | 2.8491 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
