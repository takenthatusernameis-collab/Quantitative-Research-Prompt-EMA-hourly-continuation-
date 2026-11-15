# EMA Hourly Continuation — CERE/USDT P50_144

**Symbol:** CERE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4779 |
| net_win_rate | 0.3390 |
| gross_profit_factor | 0.7613 |
| gross_win_rate | 0.3542 |
| sharpe_ratio | -8.7971 |
| sortino_ratio | -3.0356 |
| max_drawdown | 0.9819 |
| cagr | -0.7938 |
| net_avg_win | 44.9009 |
| net_avg_loss | -48.1809 |
| avg_hold_time_bars | 10.7475 |
| exposure | 0.2882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
