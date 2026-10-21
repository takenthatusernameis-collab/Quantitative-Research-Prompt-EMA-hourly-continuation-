# EMA Hourly Continuation — WAVES/USDT P26_50

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5187 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.7823 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -4.5608 |
| sortino_ratio | -1.3292 |
| max_drawdown | 0.7898 |
| cagr | -0.4616 |
| net_avg_win | 47.7501 |
| net_avg_loss | -68.8527 |
| avg_hold_time_bars | 6.0192 |
| exposure | 0.1138 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
