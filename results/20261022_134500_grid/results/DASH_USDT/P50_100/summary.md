# EMA Hourly Continuation — DASH/USDT P50_100

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.4041 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8283 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -6.2620 |
| sortino_ratio | -2.2713 |
| max_drawdown | 0.9432 |
| cagr | -0.6725 |
| net_avg_win | 21.5966 |
| net_avg_loss | -43.1913 |
| avg_hold_time_bars | 5.5045 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
