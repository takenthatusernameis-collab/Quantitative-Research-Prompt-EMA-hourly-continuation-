# EMA Hourly Continuation — FLUX/USDT P50_55

**Symbol:** FLUX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 863 |
| net_profit_factor | 0.1484 |
| net_win_rate | 0.3465 |
| gross_profit_factor | 0.6620 |
| gross_win_rate | 0.4056 |
| sharpe_ratio | -13.1151 |
| sortino_ratio | -5.7054 |
| max_drawdown | 0.9996 |
| cagr | -0.9547 |
| net_avg_win | 5.8248 |
| net_avg_loss | -20.8110 |
| avg_hold_time_bars | 1.7034 |
| exposure | 0.0668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
