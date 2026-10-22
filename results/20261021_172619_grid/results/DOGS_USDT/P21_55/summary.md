# EMA Hourly Continuation — DOGS/USDT P21_55

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6813 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8458 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -2.3763 |
| sortino_ratio | -0.7140 |
| max_drawdown | 0.5056 |
| cagr | -0.2792 |
| net_avg_win | 60.7204 |
| net_avg_loss | -77.7679 |
| avg_hold_time_bars | 8.2644 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
