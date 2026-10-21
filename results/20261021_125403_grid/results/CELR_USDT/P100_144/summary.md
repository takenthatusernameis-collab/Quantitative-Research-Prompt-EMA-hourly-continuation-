# EMA Hourly Continuation — CELR/USDT P100_144

**Symbol:** CELR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.4325 |
| gross_profit_factor | 0.7426 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -3.1098 |
| sortino_ratio | -0.7509 |
| max_drawdown | 0.5943 |
| cagr | -0.2926 |
| net_avg_win | 55.5427 |
| net_avg_loss | -77.8456 |
| avg_hold_time_bars | 6.1696 |
| exposure | 0.0807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
