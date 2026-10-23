# EMA Hourly Continuation — G/USDT P20_21

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 949 |
| net_profit_factor | 0.1953 |
| net_win_rate | 0.3456 |
| gross_profit_factor | 0.7246 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -14.6745 |
| sortino_ratio | -7.1751 |
| max_drawdown | 0.9998 |
| cagr | -0.9795 |
| net_avg_win | 7.3994 |
| net_avg_loss | -20.0078 |
| avg_hold_time_bars | 2.6754 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
