# EMA Hourly Continuation — CHZ/USDT P21_100

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.8352 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0436 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.1530 |
| sortino_ratio | -0.3420 |
| max_drawdown | 0.3861 |
| cagr | -0.1475 |
| net_avg_win | 76.7339 |
| net_avg_loss | -95.8331 |
| avg_hold_time_bars | 20.6979 |
| exposure | 0.4017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
