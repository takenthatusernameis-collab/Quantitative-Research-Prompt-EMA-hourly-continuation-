# EMA Hourly Continuation — AEVO/USDT P89_100

**Symbol:** AEVO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.3415 |
| net_win_rate | 0.4069 |
| gross_profit_factor | 0.7986 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -8.1872 |
| sortino_ratio | -2.9469 |
| max_drawdown | 0.9778 |
| cagr | -0.7768 |
| net_avg_win | 19.6420 |
| net_avg_loss | -39.4684 |
| avg_hold_time_bars | 2.4637 |
| exposure | 0.0707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
