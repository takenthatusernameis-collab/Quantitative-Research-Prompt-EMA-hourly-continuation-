# EMA Hourly Continuation — AEVO/USDT P21_144

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8284 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -1.1701 |
| sortino_ratio | -0.3206 |
| max_drawdown | 0.3582 |
| cagr | -0.1391 |
| net_avg_win | 82.9912 |
| net_avg_loss | -98.5687 |
| avg_hold_time_bars | 33.1436 |
| exposure | 0.5534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
