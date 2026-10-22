# EMA Hourly Continuation — CFX/USDT P20_200

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9737 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.3620 |
| sortino_ratio | -0.6648 |
| max_drawdown | 0.5715 |
| cagr | -0.2710 |
| net_avg_win | 64.7726 |
| net_avg_loss | -89.4034 |
| avg_hold_time_bars | 34.2095 |
| exposure | 0.6235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
