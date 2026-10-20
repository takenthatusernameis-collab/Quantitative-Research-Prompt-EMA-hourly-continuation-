# EMA Hourly Continuation — ANKR/USDT P50_55

**Symbol:** ANKR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.1950 |
| net_win_rate | 0.3072 |
| gross_profit_factor | 0.6587 |
| gross_win_rate | 0.3953 |
| sharpe_ratio | -13.4125 |
| sortino_ratio | -5.7227 |
| max_drawdown | 0.9996 |
| cagr | -0.9545 |
| net_avg_win | 9.6494 |
| net_avg_loss | -21.9395 |
| avg_hold_time_bars | 3.7246 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
