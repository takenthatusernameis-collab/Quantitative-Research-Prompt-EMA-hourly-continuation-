# EMA Hourly Continuation — DAG/USDT P34_50

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.8994 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -1.4740 |
| sortino_ratio | -0.2685 |
| max_drawdown | 0.2758 |
| cagr | -0.1162 |
| net_avg_win | 73.7509 |
| net_avg_loss | -99.0442 |
| avg_hold_time_bars | 5.8896 |
| exposure | 0.0436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
