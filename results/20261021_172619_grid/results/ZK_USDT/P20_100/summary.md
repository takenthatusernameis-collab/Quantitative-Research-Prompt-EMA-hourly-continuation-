# EMA Hourly Continuation — ZK/USDT P20_100

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.4100 |
| sortino_ratio | -0.4660 |
| max_drawdown | 0.4448 |
| cagr | -0.1951 |
| net_avg_win | 79.0789 |
| net_avg_loss | -95.4609 |
| avg_hold_time_bars | 16.7968 |
| exposure | 0.4070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
