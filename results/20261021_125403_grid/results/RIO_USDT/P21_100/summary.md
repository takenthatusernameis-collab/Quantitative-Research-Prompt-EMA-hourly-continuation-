# EMA Hourly Continuation — RIO/USDT P21_100

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8299 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.3796 |
| sortino_ratio | -0.4306 |
| max_drawdown | 0.4830 |
| cagr | -0.1824 |
| net_avg_win | 83.9011 |
| net_avg_loss | -93.7321 |
| avg_hold_time_bars | 16.2878 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
