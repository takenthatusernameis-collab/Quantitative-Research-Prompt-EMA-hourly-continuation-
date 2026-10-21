# EMA Hourly Continuation — KAS/USDT P20_50

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8554 |
| net_win_rate | 0.5339 |
| gross_profit_factor | 1.1321 |
| gross_win_rate | 0.5339 |
| sharpe_ratio | -1.0143 |
| sortino_ratio | -0.3186 |
| max_drawdown | 0.3313 |
| cagr | -0.1381 |
| net_avg_win | 73.0953 |
| net_avg_loss | -97.8858 |
| avg_hold_time_bars | 6.9174 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
