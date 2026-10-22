# EMA Hourly Continuation — STRK/USDT P34_100

**Symbol:** STRK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6426 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9504 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -3.7550 |
| sortino_ratio | -1.3319 |
| max_drawdown | 0.8148 |
| cagr | -0.4702 |
| net_avg_win | 47.1414 |
| net_avg_loss | -68.2036 |
| avg_hold_time_bars | 9.1442 |
| exposure | 0.2623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
