# EMA Hourly Continuation — OSMO/USDT P8_144

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7071 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.6206 |
| sortino_ratio | -0.8156 |
| max_drawdown | 0.6418 |
| cagr | -0.3229 |
| net_avg_win | 63.6048 |
| net_avg_loss | -84.5963 |
| avg_hold_time_bars | 33.3476 |
| exposure | 0.7412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
