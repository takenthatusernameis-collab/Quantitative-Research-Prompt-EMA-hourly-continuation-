# EMA Hourly Continuation — ZRO/USDT P8_26

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.8656 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0838 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.1465 |
| sortino_ratio | -0.4027 |
| max_drawdown | 0.4441 |
| cagr | -0.1723 |
| net_avg_win | 79.9883 |
| net_avg_loss | -99.7069 |
| avg_hold_time_bars | 7.1881 |
| exposure | 0.1946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
