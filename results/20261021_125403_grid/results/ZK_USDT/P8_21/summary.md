# EMA Hourly Continuation — ZK/USDT P8_21

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -3.1620 |
| sortino_ratio | -1.1734 |
| max_drawdown | 0.7289 |
| cagr | -0.4152 |
| net_avg_win | 49.5093 |
| net_avg_loss | -66.8857 |
| avg_hold_time_bars | 4.9094 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
