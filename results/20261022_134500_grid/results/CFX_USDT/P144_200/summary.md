# EMA Hourly Continuation — CFX/USDT P144_200

**Symbol:** CFX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.3603 |
| net_win_rate | 0.4072 |
| gross_profit_factor | 0.6561 |
| gross_win_rate | 0.4149 |
| sharpe_ratio | -5.7097 |
| sortino_ratio | -1.6008 |
| max_drawdown | 0.8657 |
| cagr | -0.5433 |
| net_avg_win | 30.6726 |
| net_avg_loss | -58.4759 |
| avg_hold_time_bars | 4.8918 |
| exposure | 0.0863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
