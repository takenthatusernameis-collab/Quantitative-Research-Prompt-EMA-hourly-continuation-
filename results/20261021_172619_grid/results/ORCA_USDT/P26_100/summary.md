# EMA Hourly Continuation — ORCA/USDT P26_100

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.8515 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.0908 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -1.1300 |
| sortino_ratio | -0.3550 |
| max_drawdown | 0.4687 |
| cagr | -0.1544 |
| net_avg_win | 78.1999 |
| net_avg_loss | -101.5101 |
| avg_hold_time_bars | 16.3438 |
| exposure | 0.3566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
