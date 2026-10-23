# EMA Hourly Continuation — SUSHI/USDT P26_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.3005 |
| net_win_rate | 0.3925 |
| gross_profit_factor | 0.8225 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -11.9333 |
| sortino_ratio | -5.7351 |
| max_drawdown | 0.9994 |
| cagr | -0.9465 |
| net_avg_win | 9.7596 |
| net_avg_loss | -20.9810 |
| avg_hold_time_bars | 2.1463 |
| exposure | 0.1089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
