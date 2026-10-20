# EMA Hourly Continuation — WEMIX/USDT P50_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.2412 |
| net_win_rate | 0.2886 |
| gross_profit_factor | 0.4488 |
| gross_win_rate | 0.3096 |
| sharpe_ratio | -13.9700 |
| sortino_ratio | -6.4020 |
| max_drawdown | 0.9997 |
| cagr | -0.9625 |
| net_avg_win | 11.0338 |
| net_avg_loss | -18.5565 |
| avg_hold_time_bars | 5.2545 |
| exposure | 0.2384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
