# EMA Hourly Continuation — AEVO/USDT P8_12

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1779 |
| net_profit_factor | 0.3282 |
| net_win_rate | 0.3895 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4283 |
| sharpe_ratio | -15.1995 |
| sortino_ratio | -9.0989 |
| max_drawdown | 1.0000 |
| cagr | -0.9913 |
| net_avg_win | 7.0494 |
| net_avg_loss | -13.7064 |
| avg_hold_time_bars | 2.1894 |
| exposure | 0.1763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
