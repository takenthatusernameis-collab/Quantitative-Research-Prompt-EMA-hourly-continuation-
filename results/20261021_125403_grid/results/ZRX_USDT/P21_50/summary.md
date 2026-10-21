# EMA Hourly Continuation — ZRX/USDT P21_50

**Symbol:** ZRX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -3.8526 |
| sortino_ratio | -1.3608 |
| max_drawdown | 0.8003 |
| cagr | -0.4653 |
| net_avg_win | 48.9019 |
| net_avg_loss | -67.2646 |
| avg_hold_time_bars | 7.3361 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
