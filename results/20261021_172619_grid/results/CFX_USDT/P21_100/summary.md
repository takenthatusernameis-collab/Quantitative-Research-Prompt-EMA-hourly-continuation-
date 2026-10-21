# EMA Hourly Continuation — CFX/USDT P21_100

**Symbol:** CFX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8050 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0036 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.4811 |
| sortino_ratio | -0.4453 |
| max_drawdown | 0.4483 |
| cagr | -0.1859 |
| net_avg_win | 75.3587 |
| net_avg_loss | -94.0341 |
| avg_hold_time_bars | 19.8889 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
