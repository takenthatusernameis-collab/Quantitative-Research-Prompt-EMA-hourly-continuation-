# EMA Hourly Continuation — DAG/USDT P8_89

**Symbol:** DAG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7484 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8701 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -1.8682 |
| sortino_ratio | -0.5878 |
| max_drawdown | 0.5555 |
| cagr | -0.2379 |
| net_avg_win | 63.6801 |
| net_avg_loss | -75.8908 |
| avg_hold_time_bars | 23.8857 |
| exposure | 0.5320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
