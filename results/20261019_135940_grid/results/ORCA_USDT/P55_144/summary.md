# EMA Hourly Continuation — ORCA/USDT P55_144

**Symbol:** ORCA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5777 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.5689 |
| sortino_ratio | -1.0980 |
| max_drawdown | 0.7541 |
| cagr | -0.4075 |
| net_avg_win | 44.6650 |
| net_avg_loss | -67.9178 |
| avg_hold_time_bars | 12.2526 |
| exposure | 0.2668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
