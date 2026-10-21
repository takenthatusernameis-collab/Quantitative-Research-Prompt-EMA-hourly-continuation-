# EMA Hourly Continuation — ARKM/USDT P34_50

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.6660 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8967 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.1562 |
| sortino_ratio | -0.4946 |
| max_drawdown | 0.4663 |
| cagr | -0.2029 |
| net_avg_win | 71.5560 |
| net_avg_loss | -94.8920 |
| avg_hold_time_bars | 5.2287 |
| exposure | 0.0613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
