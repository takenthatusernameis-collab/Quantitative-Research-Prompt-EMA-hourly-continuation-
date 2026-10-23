# EMA Hourly Continuation — CELR/USDT P12_21

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1453 |
| net_profit_factor | 0.3347 |
| net_win_rate | 0.4067 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -12.1275 |
| sortino_ratio | -6.5731 |
| max_drawdown | 0.9997 |
| cagr | -0.9620 |
| net_avg_win | 8.5112 |
| net_avg_loss | -17.4333 |
| avg_hold_time_bars | 2.7061 |
| exposure | 0.1779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
