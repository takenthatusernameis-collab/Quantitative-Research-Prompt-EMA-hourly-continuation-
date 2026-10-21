# EMA Hourly Continuation — MASK/USDT P26_144

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6446 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.5652 |
| sortino_ratio | -0.7453 |
| max_drawdown | 0.6014 |
| cagr | -0.2934 |
| net_avg_win | 53.0362 |
| net_avg_loss | -74.4249 |
| avg_hold_time_bars | 23.4248 |
| exposure | 0.4461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
