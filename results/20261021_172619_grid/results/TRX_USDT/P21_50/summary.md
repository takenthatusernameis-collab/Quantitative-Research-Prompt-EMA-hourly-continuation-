# EMA Hourly Continuation — TRX/USDT P21_50

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.4342 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -5.2510 |
| sortino_ratio | -1.5517 |
| max_drawdown | 0.8398 |
| cagr | -0.5079 |
| net_avg_win | 32.8932 |
| net_avg_loss | -68.9973 |
| avg_hold_time_bars | 8.1523 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
