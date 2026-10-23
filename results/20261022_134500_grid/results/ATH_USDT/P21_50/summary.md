# EMA Hourly Continuation — ATH/USDT P21_50

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.5575 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -5.7953 |
| sortino_ratio | -2.5441 |
| max_drawdown | 0.9471 |
| cagr | -0.7061 |
| net_avg_win | 27.5954 |
| net_avg_loss | -45.1995 |
| avg_hold_time_bars | 4.4308 |
| exposure | 0.1939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
