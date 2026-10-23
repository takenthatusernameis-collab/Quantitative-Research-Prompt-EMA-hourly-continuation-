# EMA Hourly Continuation — EWT/USDT P55_200

**Symbol:** EWT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.5594 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7970 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -3.7680 |
| sortino_ratio | -1.0675 |
| max_drawdown | 0.7601 |
| cagr | -0.4036 |
| net_avg_win | 51.5614 |
| net_avg_loss | -71.7341 |
| avg_hold_time_bars | 16.5477 |
| exposure | 0.3076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
