# EMA Hourly Continuation — CELR/USDT P55_144

**Symbol:** CELR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -3.0863 |
| sortino_ratio | -0.9639 |
| max_drawdown | 0.6841 |
| cagr | -0.3626 |
| net_avg_win | 49.0337 |
| net_avg_loss | -71.5167 |
| avg_hold_time_bars | 13.1379 |
| exposure | 0.2889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
