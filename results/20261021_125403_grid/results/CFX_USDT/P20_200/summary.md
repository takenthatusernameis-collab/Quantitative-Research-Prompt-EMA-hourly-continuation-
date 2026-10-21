# EMA Hourly Continuation — CFX/USDT P20_200

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9440 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.3885 |
| sortino_ratio | -0.3484 |
| max_drawdown | 0.3790 |
| cagr | -0.1483 |
| net_avg_win | 78.0473 |
| net_avg_loss | -94.9864 |
| avg_hold_time_bars | 43.8161 |
| exposure | 0.6174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
