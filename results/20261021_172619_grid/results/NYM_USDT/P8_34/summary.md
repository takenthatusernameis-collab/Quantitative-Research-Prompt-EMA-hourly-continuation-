# EMA Hourly Continuation — NYM/USDT P8_34

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.5655 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -3.8427 |
| sortino_ratio | -1.3222 |
| max_drawdown | 0.7939 |
| cagr | -0.4588 |
| net_avg_win | 36.0214 |
| net_avg_loss | -60.7070 |
| avg_hold_time_bars | 14.9553 |
| exposure | 0.3956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
