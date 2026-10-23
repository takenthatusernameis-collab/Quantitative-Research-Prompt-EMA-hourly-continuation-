# EMA Hourly Continuation — FLIP/USDT P20_50

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.4078 |
| net_win_rate | 0.4038 |
| gross_profit_factor | 0.7854 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -7.7946 |
| sortino_ratio | -2.8399 |
| max_drawdown | 0.9757 |
| cagr | -0.7697 |
| net_avg_win | 24.5902 |
| net_avg_loss | -40.8509 |
| avg_hold_time_bars | 9.0562 |
| exposure | 0.2783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
