# EMA Hourly Continuation — CFX/USDT P8_20

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.8265 |
| net_win_rate | 0.5329 |
| gross_profit_factor | 1.1427 |
| gross_win_rate | 0.5329 |
| sharpe_ratio | -1.3465 |
| sortino_ratio | -0.4296 |
| max_drawdown | 0.4178 |
| cagr | -0.1789 |
| net_avg_win | 71.8227 |
| net_avg_loss | -99.1459 |
| avg_hold_time_bars | 5.4938 |
| exposure | 0.1214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
