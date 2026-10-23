# EMA Hourly Continuation — OSMO/USDT P8_26

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1515 |
| net_profit_factor | 0.5398 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 1.1591 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -10.8011 |
| sortino_ratio | -5.9244 |
| max_drawdown | 0.9994 |
| cagr | -0.9477 |
| net_avg_win | 18.0070 |
| net_avg_loss | -25.1348 |
| avg_hold_time_bars | 4.3710 |
| exposure | 0.3010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
