# EMA Hourly Continuation — XNO/USDT P26_34

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.4950 |
| net_win_rate | 0.3982 |
| gross_profit_factor | 0.7040 |
| gross_win_rate | 0.3982 |
| sharpe_ratio | -3.4593 |
| sortino_ratio | -0.7316 |
| max_drawdown | 0.5760 |
| cagr | -0.2869 |
| net_avg_win | 63.7363 |
| net_avg_loss | -85.1970 |
| avg_hold_time_bars | 4.7828 |
| exposure | 0.0480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
