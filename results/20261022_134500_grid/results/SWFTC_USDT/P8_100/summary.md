# EMA Hourly Continuation — SWFTC/USDT P8_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.7857 |
| gross_win_rate | 0.4261 |
| sharpe_ratio | -7.2139 |
| sortino_ratio | -3.0371 |
| max_drawdown | 0.9776 |
| cagr | -0.7781 |
| net_avg_win | 26.6229 |
| net_avg_loss | -37.0756 |
| avg_hold_time_bars | 13.2563 |
| exposure | 0.5501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
