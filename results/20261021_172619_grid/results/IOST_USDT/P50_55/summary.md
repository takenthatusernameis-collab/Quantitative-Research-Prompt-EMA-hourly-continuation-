# EMA Hourly Continuation — IOST/USDT P50_55

**Symbol:** IOST/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.5045 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -2.8992 |
| sortino_ratio | -0.5809 |
| max_drawdown | 0.5008 |
| cagr | -0.2363 |
| net_avg_win | 56.2665 |
| net_avg_loss | -95.4482 |
| avg_hold_time_bars | 4.4041 |
| exposure | 0.0386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
