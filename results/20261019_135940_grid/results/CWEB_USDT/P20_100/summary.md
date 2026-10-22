# EMA Hourly Continuation — CWEB/USDT P20_100

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5585 |
| net_win_rate | 0.4360 |
| gross_profit_factor | 0.8975 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -4.9660 |
| sortino_ratio | -1.5804 |
| max_drawdown | 0.8643 |
| cagr | -0.5409 |
| net_avg_win | 48.2629 |
| net_avg_loss | -66.8161 |
| avg_hold_time_bars | 20.1047 |
| exposure | 0.4715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
