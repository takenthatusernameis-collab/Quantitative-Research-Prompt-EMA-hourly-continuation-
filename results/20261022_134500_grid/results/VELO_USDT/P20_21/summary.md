# EMA Hourly Continuation — VELO/USDT P20_21

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1292 |
| net_profit_factor | 0.2779 |
| net_win_rate | 0.3243 |
| gross_profit_factor | 0.6488 |
| gross_win_rate | 0.3661 |
| sharpe_ratio | -16.7058 |
| sortino_ratio | -8.7981 |
| max_drawdown | 1.0000 |
| cagr | -0.9932 |
| net_avg_win | 9.1859 |
| net_avg_loss | -15.8635 |
| avg_hold_time_bars | 1.6610 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
