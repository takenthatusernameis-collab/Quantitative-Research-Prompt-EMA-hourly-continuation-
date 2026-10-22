# EMA Hourly Continuation — LUNA/USDT P26_144

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7948 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.3587 |
| sortino_ratio | -0.3790 |
| max_drawdown | 0.3630 |
| cagr | -0.1605 |
| net_avg_win | 72.4938 |
| net_avg_loss | -91.6927 |
| avg_hold_time_bars | 24.3879 |
| exposure | 0.4201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
