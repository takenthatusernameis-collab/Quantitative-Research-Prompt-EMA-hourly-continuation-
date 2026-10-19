# EMA Hourly Continuation — LINK/USDT P20_55

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.5490 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.9501 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -6.9883 |
| sortino_ratio | -2.8483 |
| max_drawdown | 0.9723 |
| cagr | -0.7558 |
| net_avg_win | 31.0172 |
| net_avg_loss | -46.2955 |
| avg_hold_time_bars | 6.0083 |
| exposure | 0.2310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
