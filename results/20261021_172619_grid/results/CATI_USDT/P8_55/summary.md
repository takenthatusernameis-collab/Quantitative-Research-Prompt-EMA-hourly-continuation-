# EMA Hourly Continuation — CATI/USDT P8_55

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -3.5788 |
| sortino_ratio | -1.2334 |
| max_drawdown | 0.7209 |
| cagr | -0.4356 |
| net_avg_win | 56.4408 |
| net_avg_loss | -69.1442 |
| avg_hold_time_bars | 16.4300 |
| exposure | 0.4440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
