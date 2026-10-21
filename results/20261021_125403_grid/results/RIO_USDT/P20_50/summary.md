# EMA Hourly Continuation — RIO/USDT P20_50

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.7813 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -1.7396 |
| sortino_ratio | -0.5231 |
| max_drawdown | 0.4740 |
| cagr | -0.2152 |
| net_avg_win | 76.9878 |
| net_avg_loss | -89.1942 |
| avg_hold_time_bars | 8.5452 |
| exposure | 0.1734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
