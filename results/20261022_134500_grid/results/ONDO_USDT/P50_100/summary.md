# EMA Hourly Continuation — ONDO/USDT P50_100

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.4785 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7627 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -5.9231 |
| sortino_ratio | -2.1401 |
| max_drawdown | 0.9249 |
| cagr | -0.6413 |
| net_avg_win | 30.3809 |
| net_avg_loss | -47.1128 |
| avg_hold_time_bars | 5.5634 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
