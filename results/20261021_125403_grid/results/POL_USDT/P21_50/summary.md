# EMA Hourly Continuation — POL/USDT P21_50

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -2.6225 |
| sortino_ratio | -0.8132 |
| max_drawdown | 0.6337 |
| cagr | -0.3109 |
| net_avg_win | 50.3222 |
| net_avg_loss | -72.3076 |
| avg_hold_time_bars | 8.9574 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
