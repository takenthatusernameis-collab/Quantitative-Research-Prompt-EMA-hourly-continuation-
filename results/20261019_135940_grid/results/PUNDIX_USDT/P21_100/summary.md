# EMA Hourly Continuation — PUNDIX/USDT P21_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.5495 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8611 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -4.8108 |
| sortino_ratio | -1.7261 |
| max_drawdown | 0.8805 |
| cagr | -0.5652 |
| net_avg_win | 36.1229 |
| net_avg_loss | -54.8092 |
| avg_hold_time_bars | 14.9109 |
| exposure | 0.4412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
