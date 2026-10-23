# EMA Hourly Continuation — AEVO/USDT P21_144

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7473 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0385 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -2.1017 |
| sortino_ratio | -0.6332 |
| max_drawdown | 0.5748 |
| cagr | -0.2610 |
| net_avg_win | 69.5380 |
| net_avg_loss | -90.2676 |
| avg_hold_time_bars | 26.9089 |
| exposure | 0.5613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
