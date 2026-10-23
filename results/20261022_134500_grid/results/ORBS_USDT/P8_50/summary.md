# EMA Hourly Continuation — ORBS/USDT P8_50

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.4945 |
| net_win_rate | 0.4084 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -9.0677 |
| sortino_ratio | -4.2594 |
| max_drawdown | 0.9950 |
| cagr | -0.8773 |
| net_avg_win | 21.3904 |
| net_avg_loss | -29.8651 |
| avg_hold_time_bars | 9.7567 |
| exposure | 0.4940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
