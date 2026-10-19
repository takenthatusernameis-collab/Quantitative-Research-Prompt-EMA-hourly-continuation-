# EMA Hourly Continuation — DASH/USDT P20_200

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.4702 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.7955 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -4.2320 |
| sortino_ratio | -1.2013 |
| max_drawdown | 0.7920 |
| cagr | -0.4524 |
| net_avg_win | 36.6181 |
| net_avg_loss | -63.4369 |
| avg_hold_time_bars | 32.3967 |
| exposure | 0.6200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
