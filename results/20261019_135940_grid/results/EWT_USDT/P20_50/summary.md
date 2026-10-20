# EMA Hourly Continuation — EWT/USDT P20_50

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.4646 |
| net_win_rate | 0.4196 |
| gross_profit_factor | 0.8086 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -8.1651 |
| sortino_ratio | -3.4276 |
| max_drawdown | 0.9869 |
| cagr | -0.8208 |
| net_avg_win | 22.7690 |
| net_avg_loss | -35.4381 |
| avg_hold_time_bars | 5.2455 |
| exposure | 0.2136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
