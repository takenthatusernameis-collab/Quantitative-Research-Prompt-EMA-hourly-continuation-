# EMA Hourly Continuation — CELR/USDT P20_50

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -3.1252 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.7330 |
| cagr | -0.3935 |
| net_avg_win | 57.4476 |
| net_avg_loss | -75.2085 |
| avg_hold_time_bars | 8.1522 |
| exposure | 0.2206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
