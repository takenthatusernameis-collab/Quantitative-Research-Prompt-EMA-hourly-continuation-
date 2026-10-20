# EMA Hourly Continuation — BOME/USDT P20_21

**Symbol:** BOME/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.1668 |
| net_win_rate | 0.3131 |
| gross_profit_factor | 0.6107 |
| gross_win_rate | 0.3747 |
| sharpe_ratio | -16.2763 |
| sortino_ratio | -8.2415 |
| max_drawdown | 1.0000 |
| cagr | -0.9905 |
| net_avg_win | 5.3957 |
| net_avg_loss | -14.7441 |
| avg_hold_time_bars | 1.5907 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
