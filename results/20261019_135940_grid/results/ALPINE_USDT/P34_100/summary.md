# EMA Hourly Continuation — ALPINE/USDT P34_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5643 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -5.1963 |
| sortino_ratio | -1.8706 |
| max_drawdown | 0.9013 |
| cagr | -0.5984 |
| net_avg_win | 38.4251 |
| net_avg_loss | -57.7909 |
| avg_hold_time_bars | 9.9833 |
| exposure | 0.2995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
