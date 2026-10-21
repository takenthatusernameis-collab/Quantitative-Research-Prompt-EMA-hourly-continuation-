# EMA Hourly Continuation — LUNC/USDT P21_55

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8348 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -3.4351 |
| sortino_ratio | -1.0649 |
| max_drawdown | 0.7196 |
| cagr | -0.3864 |
| net_avg_win | 52.0134 |
| net_avg_loss | -70.2620 |
| avg_hold_time_bars | 7.7400 |
| exposure | 0.1664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
