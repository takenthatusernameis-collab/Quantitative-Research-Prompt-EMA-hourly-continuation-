# EMA Hourly Continuation — BAND/USDT P26_100

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.6096 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9376 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -4.1444 |
| sortino_ratio | -1.4475 |
| max_drawdown | 0.8298 |
| cagr | -0.4985 |
| net_avg_win | 44.0967 |
| net_avg_loss | -64.3977 |
| avg_hold_time_bars | 12.2484 |
| exposure | 0.3436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
