# EMA Hourly Continuation — BRETT/USDT P50_144

**Symbol:** BRETT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -1.8474 |
| sortino_ratio | -0.4716 |
| max_drawdown | 0.4201 |
| cagr | -0.1953 |
| net_avg_win | 71.8335 |
| net_avg_loss | -84.8490 |
| avg_hold_time_bars | 19.5000 |
| exposure | 0.2871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
