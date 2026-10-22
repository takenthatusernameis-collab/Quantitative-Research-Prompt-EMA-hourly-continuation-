# EMA Hourly Continuation — DASH/USDT P12_100

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.5273 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8893 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -4.8271 |
| sortino_ratio | -1.7274 |
| max_drawdown | 0.8817 |
| cagr | -0.5643 |
| net_avg_win | 33.3497 |
| net_avg_loss | -52.3454 |
| avg_hold_time_bars | 20.1515 |
| exposure | 0.5926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
