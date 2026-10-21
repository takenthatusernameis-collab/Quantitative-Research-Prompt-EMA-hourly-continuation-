# EMA Hourly Continuation — TRAC/USDT P21_100

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.8896 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.1043 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -0.7964 |
| sortino_ratio | -0.2564 |
| max_drawdown | 0.3335 |
| cagr | -0.1150 |
| net_avg_win | 81.2671 |
| net_avg_loss | -100.9843 |
| avg_hold_time_bars | 15.3126 |
| exposure | 0.3473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
