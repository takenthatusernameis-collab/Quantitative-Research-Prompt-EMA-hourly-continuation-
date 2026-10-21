# EMA Hourly Continuation — ANKR/USDT P26_50

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.5560 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -4.8117 |
| sortino_ratio | -1.5339 |
| max_drawdown | 0.8346 |
| cagr | -0.5098 |
| net_avg_win | 48.7586 |
| net_avg_loss | -65.8440 |
| avg_hold_time_bars | 8.6974 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
