# EMA Hourly Continuation — IOTA/USDT P55_144

**Symbol:** IOTA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -2.4483 |
| sortino_ratio | -0.6500 |
| max_drawdown | 0.5505 |
| cagr | -0.2582 |
| net_avg_win | 69.0465 |
| net_avg_loss | -85.5540 |
| avg_hold_time_bars | 14.8940 |
| exposure | 0.2363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
