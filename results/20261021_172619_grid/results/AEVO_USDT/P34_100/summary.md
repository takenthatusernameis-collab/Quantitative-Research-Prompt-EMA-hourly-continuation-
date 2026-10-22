# EMA Hourly Continuation — AEVO/USDT P34_100

**Symbol:** AEVO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9590 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.8155 |
| sortino_ratio | -0.5621 |
| max_drawdown | 0.4934 |
| cagr | -0.2283 |
| net_avg_win | 65.8463 |
| net_avg_loss | -83.9969 |
| avg_hold_time_bars | 13.6837 |
| exposure | 0.2916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
