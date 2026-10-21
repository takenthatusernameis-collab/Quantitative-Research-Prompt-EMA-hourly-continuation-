# EMA Hourly Continuation — DGB/USDT P26_100

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6980 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8807 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.4081 |
| sortino_ratio | -0.7261 |
| max_drawdown | 0.5674 |
| cagr | -0.2837 |
| net_avg_win | 62.4601 |
| net_avg_loss | -78.6232 |
| avg_hold_time_bars | 16.1960 |
| exposure | 0.3305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
