# EMA Hourly Continuation — CTSI/USDT P8_26

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.7463 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 1.0389 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -3.2230 |
| sortino_ratio | -1.2940 |
| max_drawdown | 0.7731 |
| cagr | -0.4461 |
| net_avg_win | 58.9336 |
| net_avg_loss | -76.5824 |
| avg_hold_time_bars | 7.2436 |
| exposure | 0.2581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
