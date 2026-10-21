# EMA Hourly Continuation — KSM/USDT P144_200

**Symbol:** KSM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -1.6931 |
| sortino_ratio | -0.3665 |
| max_drawdown | 0.3818 |
| cagr | -0.1542 |
| net_avg_win | 68.5229 |
| net_avg_loss | -98.0433 |
| avg_hold_time_bars | 6.7225 |
| exposure | 0.0694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
