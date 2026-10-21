# EMA Hourly Continuation — ZEN/USDT P34_100

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7312 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.0815 |
| sortino_ratio | -0.6283 |
| max_drawdown | 0.5441 |
| cagr | -0.2518 |
| net_avg_win | 65.4653 |
| net_avg_loss | -82.6118 |
| avg_hold_time_bars | 13.4018 |
| exposure | 0.2729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
