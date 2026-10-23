# EMA Hourly Continuation — BRETT/USDT P50_144

**Symbol:** BRETT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8271 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -3.1795 |
| sortino_ratio | -0.9663 |
| max_drawdown | 0.6588 |
| cagr | -0.3630 |
| net_avg_win | 52.4299 |
| net_avg_loss | -71.4403 |
| avg_hold_time_bars | 14.2357 |
| exposure | 0.2993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
