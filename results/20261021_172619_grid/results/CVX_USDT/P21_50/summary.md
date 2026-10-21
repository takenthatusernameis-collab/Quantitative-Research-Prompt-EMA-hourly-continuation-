# EMA Hourly Continuation — CVX/USDT P21_50

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7528 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -2.1442 |
| sortino_ratio | -0.7061 |
| max_drawdown | 0.5665 |
| cagr | -0.2771 |
| net_avg_win | 64.7862 |
| net_avg_loss | -84.7648 |
| avg_hold_time_bars | 6.8807 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
