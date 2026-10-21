# EMA Hourly Continuation — AXS/USDT P8_12

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6569 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9724 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -1.9906 |
| sortino_ratio | -0.4419 |
| max_drawdown | 0.4078 |
| cagr | -0.1837 |
| net_avg_win | 64.4777 |
| net_avg_loss | -96.5337 |
| avg_hold_time_bars | 4.3375 |
| exposure | 0.0471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
