# EMA Hourly Continuation — XPR/USDT P34_100

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6682 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -2.3211 |
| sortino_ratio | -0.5945 |
| max_drawdown | 0.5024 |
| cagr | -0.2392 |
| net_avg_win | 66.2379 |
| net_avg_loss | -86.5250 |
| avg_hold_time_bars | 13.0586 |
| exposure | 0.1923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
