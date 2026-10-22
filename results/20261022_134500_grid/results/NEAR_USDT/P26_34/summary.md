# EMA Hourly Continuation — NEAR/USDT P26_34

**Symbol:** NEAR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.2875 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.7308 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -12.5211 |
| sortino_ratio | -5.9136 |
| max_drawdown | 0.9996 |
| cagr | -0.9559 |
| net_avg_win | 9.7898 |
| net_avg_loss | -20.8461 |
| avg_hold_time_bars | 1.9834 |
| exposure | 0.0978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
