# EMA Hourly Continuation — CGPT/USDT P50_100

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5137 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -4.9180 |
| sortino_ratio | -1.6848 |
| max_drawdown | 0.8763 |
| cagr | -0.5634 |
| net_avg_win | 33.9862 |
| net_avg_loss | -55.3737 |
| avg_hold_time_bars | 6.5159 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
