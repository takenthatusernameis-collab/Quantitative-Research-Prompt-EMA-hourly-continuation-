# EMA Hourly Continuation — ARPA/USDT P8_26

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.6432 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -4.4549 |
| sortino_ratio | -1.8652 |
| max_drawdown | 0.8875 |
| cagr | -0.5739 |
| net_avg_win | 38.9445 |
| net_avg_loss | -54.9131 |
| avg_hold_time_bars | 6.2209 |
| exposure | 0.2421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
