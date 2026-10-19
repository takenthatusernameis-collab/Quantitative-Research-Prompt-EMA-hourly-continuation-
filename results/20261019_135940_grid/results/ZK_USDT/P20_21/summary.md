# EMA Hourly Continuation — ZK/USDT P20_21

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.2716 |
| net_win_rate | 0.3221 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.3998 |
| sharpe_ratio | -16.5121 |
| sortino_ratio | -8.6566 |
| max_drawdown | 1.0000 |
| cagr | -0.9916 |
| net_avg_win | 9.7855 |
| net_avg_loss | -17.1174 |
| avg_hold_time_bars | 1.7726 |
| exposure | 0.1022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
