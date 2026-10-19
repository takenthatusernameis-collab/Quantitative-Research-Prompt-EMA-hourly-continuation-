# EMA Hourly Continuation — STRK/USDT P34_55

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.4781 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -7.4189 |
| sortino_ratio | -3.0980 |
| max_drawdown | 0.9777 |
| cagr | -0.7759 |
| net_avg_win | 23.7358 |
| net_avg_loss | -38.9079 |
| avg_hold_time_bars | 2.8730 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
