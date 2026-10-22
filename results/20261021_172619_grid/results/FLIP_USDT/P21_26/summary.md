# EMA Hourly Continuation — FLIP/USDT P21_26

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.3600 |
| net_win_rate | 0.3981 |
| gross_profit_factor | 0.7284 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -5.6462 |
| sortino_ratio | -1.4446 |
| max_drawdown | 0.8360 |
| cagr | -0.5112 |
| net_avg_win | 36.9464 |
| net_avg_loss | -67.8922 |
| avg_hold_time_bars | 7.7273 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
