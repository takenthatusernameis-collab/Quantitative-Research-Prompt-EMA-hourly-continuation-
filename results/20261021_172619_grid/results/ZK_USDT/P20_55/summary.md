# EMA Hourly Continuation — ZK/USDT P20_55

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7812 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -2.0349 |
| sortino_ratio | -0.6928 |
| max_drawdown | 0.5603 |
| cagr | -0.2725 |
| net_avg_win | 72.1395 |
| net_avg_loss | -89.5824 |
| avg_hold_time_bars | 8.2822 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
