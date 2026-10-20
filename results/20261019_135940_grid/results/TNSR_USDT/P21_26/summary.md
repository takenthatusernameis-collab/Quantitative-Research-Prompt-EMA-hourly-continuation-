# EMA Hourly Continuation — TNSR/USDT P21_26

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1162 |
| net_profit_factor | 0.3716 |
| net_win_rate | 0.3821 |
| gross_profit_factor | 0.7942 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -12.2720 |
| sortino_ratio | -5.9514 |
| max_drawdown | 0.9996 |
| cagr | -0.9553 |
| net_avg_win | 13.3120 |
| net_avg_loss | -22.1540 |
| avg_hold_time_bars | 2.0499 |
| exposure | 0.1078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
