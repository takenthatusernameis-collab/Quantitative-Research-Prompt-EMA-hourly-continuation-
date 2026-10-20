# EMA Hourly Continuation — CPOOL/USDT P20_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8544 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -3.2334 |
| sortino_ratio | -1.0317 |
| max_drawdown | 0.7418 |
| cagr | -0.3933 |
| net_avg_win | 56.7289 |
| net_avg_loss | -73.3717 |
| avg_hold_time_bars | 23.6386 |
| exposure | 0.5620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
