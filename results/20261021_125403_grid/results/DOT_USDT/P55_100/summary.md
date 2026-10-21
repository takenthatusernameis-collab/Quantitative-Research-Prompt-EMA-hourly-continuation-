# EMA Hourly Continuation — DOT/USDT P55_100

**Symbol:** DOT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7901 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.0831 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -1.1812 |
| sortino_ratio | -0.2967 |
| max_drawdown | 0.3212 |
| cagr | -0.1279 |
| net_avg_win | 68.8860 |
| net_avg_loss | -96.2633 |
| avg_hold_time_bars | 8.4356 |
| exposure | 0.1162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
