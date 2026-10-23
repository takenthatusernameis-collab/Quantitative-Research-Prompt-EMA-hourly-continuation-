# EMA Hourly Continuation — BLUR/USDT P34_50

**Symbol:** BLUR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 910 |
| net_profit_factor | 0.4694 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -7.4127 |
| sortino_ratio | -3.1565 |
| max_drawdown | 0.9815 |
| cagr | -0.7916 |
| net_avg_win | 20.5610 |
| net_avg_loss | -37.8801 |
| avg_hold_time_bars | 2.7527 |
| exposure | 0.1134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
