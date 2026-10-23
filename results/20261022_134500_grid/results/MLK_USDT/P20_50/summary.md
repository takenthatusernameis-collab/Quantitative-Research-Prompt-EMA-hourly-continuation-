# EMA Hourly Continuation — MLK/USDT P20_50

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1297 |
| net_profit_factor | 0.2682 |
| net_win_rate | 0.2729 |
| gross_profit_factor | 0.5903 |
| gross_win_rate | 0.2899 |
| sharpe_ratio | -16.4641 |
| sortino_ratio | -8.5897 |
| max_drawdown | 1.0000 |
| cagr | -0.9876 |
| net_avg_win | 10.3545 |
| net_avg_loss | -14.4913 |
| avg_hold_time_bars | 4.1411 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
