# EMA Hourly Continuation — ONT/USDT P8_12

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1730 |
| net_profit_factor | 0.2675 |
| net_win_rate | 0.3584 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -17.8032 |
| sortino_ratio | -10.7456 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 5.8907 |
| net_avg_loss | -12.2993 |
| avg_hold_time_bars | 2.1491 |
| exposure | 0.1682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
