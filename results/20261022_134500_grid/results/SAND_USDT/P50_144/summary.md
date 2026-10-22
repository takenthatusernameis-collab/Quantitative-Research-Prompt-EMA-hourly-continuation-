# EMA Hourly Continuation — SAND/USDT P50_144

**Symbol:** SAND/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.5736 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.7331 |
| sortino_ratio | -1.0988 |
| max_drawdown | 0.7347 |
| cagr | -0.4104 |
| net_avg_win | 48.6924 |
| net_avg_loss | -73.3250 |
| avg_hold_time_bars | 16.5594 |
| exposure | 0.3297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
