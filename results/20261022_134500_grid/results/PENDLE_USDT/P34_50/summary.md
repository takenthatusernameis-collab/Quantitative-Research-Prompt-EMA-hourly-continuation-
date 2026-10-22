# EMA Hourly Continuation — PENDLE/USDT P34_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.4310 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8217 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -8.1821 |
| sortino_ratio | -3.5712 |
| max_drawdown | 0.9881 |
| cagr | -0.8287 |
| net_avg_win | 17.8181 |
| net_avg_loss | -32.3967 |
| avg_hold_time_bars | 2.8190 |
| exposure | 0.1225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
