# EMA Hourly Continuation — AEVO/USDT P8_20

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.7478 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.5858 |
| sortino_ratio | -0.9857 |
| max_drawdown | 0.7062 |
| cagr | -0.3633 |
| net_avg_win | 56.6108 |
| net_avg_loss | -76.5661 |
| avg_hold_time_bars | 5.5692 |
| exposure | 0.1784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
