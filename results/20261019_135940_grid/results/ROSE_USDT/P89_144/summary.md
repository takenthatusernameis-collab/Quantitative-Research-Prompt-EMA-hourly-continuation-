# EMA Hourly Continuation — ROSE/USDT P89_144

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.5850 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9511 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -3.4515 |
| sortino_ratio | -1.0723 |
| max_drawdown | 0.7339 |
| cagr | -0.4023 |
| net_avg_win | 43.1396 |
| net_avg_loss | -70.7625 |
| avg_hold_time_bars | 4.9897 |
| exposure | 0.1098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
