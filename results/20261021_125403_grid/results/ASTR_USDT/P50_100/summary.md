# EMA Hourly Continuation — ASTR/USDT P50_100

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -2.3231 |
| sortino_ratio | -0.6556 |
| max_drawdown | 0.5516 |
| cagr | -0.2606 |
| net_avg_win | 59.6643 |
| net_avg_loss | -84.7765 |
| avg_hold_time_bars | 9.7410 |
| exposure | 0.1719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
