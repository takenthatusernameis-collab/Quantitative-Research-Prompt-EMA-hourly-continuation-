# EMA Hourly Continuation — AURORA/USDT P21_144

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6265 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9461 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -3.6001 |
| sortino_ratio | -1.0802 |
| max_drawdown | 0.7447 |
| cagr | -0.4083 |
| net_avg_win | 57.6675 |
| net_avg_loss | -79.0560 |
| avg_hold_time_bars | 23.3861 |
| exposure | 0.4900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
