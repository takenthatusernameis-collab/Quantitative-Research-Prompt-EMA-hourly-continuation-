# EMA Hourly Continuation — ROSE/USDT P8_21

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1743 |
| net_profit_factor | 0.3693 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.7903 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -11.1562 |
| sortino_ratio | -6.5640 |
| max_drawdown | 0.9997 |
| cagr | -0.9623 |
| net_avg_win | 7.6624 |
| net_avg_loss | -16.1914 |
| avg_hold_time_bars | 2.9105 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
