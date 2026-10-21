# EMA Hourly Continuation — DGB/USDT P34_100

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.0970 |
| sortino_ratio | -0.6066 |
| max_drawdown | 0.5094 |
| cagr | -0.2434 |
| net_avg_win | 64.2004 |
| net_avg_loss | -82.6366 |
| avg_hold_time_bars | 13.9440 |
| exposure | 0.2605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
