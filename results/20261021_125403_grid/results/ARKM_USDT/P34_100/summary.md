# EMA Hourly Continuation — ARKM/USDT P34_100

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7709 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.6585 |
| sortino_ratio | -0.4839 |
| max_drawdown | 0.4579 |
| cagr | -0.2003 |
| net_avg_win | 70.8329 |
| net_avg_loss | -88.0037 |
| avg_hold_time_bars | 12.3573 |
| exposure | 0.2342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
