# EMA Hourly Continuation — FLUX/USDT P8_55

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.8207 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0225 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.4828 |
| sortino_ratio | -0.5589 |
| max_drawdown | 0.5465 |
| cagr | -0.2296 |
| net_avg_win | 62.4880 |
| net_avg_loss | -79.5281 |
| avg_hold_time_bars | 14.0319 |
| exposure | 0.4395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
