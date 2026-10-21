# EMA Hourly Continuation — OP/USDT P34_100

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7970 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.4901 |
| sortino_ratio | -0.4337 |
| max_drawdown | 0.4374 |
| cagr | -0.1816 |
| net_avg_win | 74.9904 |
| net_avg_loss | -94.5511 |
| avg_hold_time_bars | 14.2446 |
| exposure | 0.2674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
