# EMA Hourly Continuation — QI/USDT P50_100

**Symbol:** QI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.8425 |
| sortino_ratio | -0.5128 |
| max_drawdown | 0.4712 |
| cagr | -0.2094 |
| net_avg_win | 61.8349 |
| net_avg_loss | -87.5369 |
| avg_hold_time_bars | 9.4085 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
