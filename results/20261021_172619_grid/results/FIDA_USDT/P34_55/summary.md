# EMA Hourly Continuation — FIDA/USDT P34_55

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.2894 |
| sortino_ratio | -0.6519 |
| max_drawdown | 0.5417 |
| cagr | -0.2576 |
| net_avg_win | 58.8813 |
| net_avg_loss | -85.2656 |
| avg_hold_time_bars | 6.8380 |
| exposure | 0.1222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
