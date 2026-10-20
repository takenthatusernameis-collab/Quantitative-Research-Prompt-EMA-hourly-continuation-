# EMA Hourly Continuation — NYM/USDT P55_100

**Symbol:** NYM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.1902 |
| net_win_rate | 0.3210 |
| gross_profit_factor | 0.5086 |
| gross_win_rate | 0.3581 |
| sharpe_ratio | -9.8544 |
| sortino_ratio | -3.3338 |
| max_drawdown | 0.9880 |
| cagr | -0.8270 |
| net_avg_win | 13.4117 |
| net_avg_loss | -33.3284 |
| avg_hold_time_bars | 6.6419 |
| exposure | 0.1627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
