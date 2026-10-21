# EMA Hourly Continuation — HNT/USDT P26_100

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.8957 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.7476 |
| sortino_ratio | -0.5114 |
| max_drawdown | 0.4935 |
| cagr | -0.2107 |
| net_avg_win | 63.4406 |
| net_avg_loss | -79.2632 |
| avg_hold_time_bars | 18.0521 |
| exposure | 0.3463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
