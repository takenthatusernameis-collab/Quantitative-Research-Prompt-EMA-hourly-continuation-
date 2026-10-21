# EMA Hourly Continuation — ONDO/USDT P34_100

**Symbol:** ONDO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.1895 |
| sortino_ratio | -0.6203 |
| max_drawdown | 0.5337 |
| cagr | -0.2477 |
| net_avg_win | 67.9230 |
| net_avg_loss | -82.6478 |
| avg_hold_time_bars | 12.7809 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
