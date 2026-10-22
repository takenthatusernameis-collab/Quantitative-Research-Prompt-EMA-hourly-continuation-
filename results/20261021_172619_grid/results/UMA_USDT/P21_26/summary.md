# EMA Hourly Continuation — UMA/USDT P21_26

**Symbol:** UMA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.4913 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8042 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.9513 |
| sortino_ratio | -0.9910 |
| max_drawdown | 0.6882 |
| cagr | -0.3706 |
| net_avg_win | 48.1111 |
| net_avg_loss | -79.9613 |
| avg_hold_time_bars | 5.4788 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
