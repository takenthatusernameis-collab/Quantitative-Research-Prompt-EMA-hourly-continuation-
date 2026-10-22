# EMA Hourly Continuation — LUNC/USDT P8_21

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1832 |
| net_profit_factor | 0.3255 |
| net_win_rate | 0.4056 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -14.6222 |
| sortino_ratio | -8.8954 |
| max_drawdown | 1.0000 |
| cagr | -0.9898 |
| net_avg_win | 6.4936 |
| net_avg_loss | -13.6130 |
| avg_hold_time_bars | 2.6070 |
| exposure | 0.2171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
