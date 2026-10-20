# EMA Hourly Continuation — CGPT/USDT P55_100

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5169 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4666 |
| sharpe_ratio | -5.1361 |
| sortino_ratio | -1.7587 |
| max_drawdown | 0.8916 |
| cagr | -0.5820 |
| net_avg_win | 34.6761 |
| net_avg_loss | -56.7358 |
| avg_hold_time_bars | 5.2843 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
