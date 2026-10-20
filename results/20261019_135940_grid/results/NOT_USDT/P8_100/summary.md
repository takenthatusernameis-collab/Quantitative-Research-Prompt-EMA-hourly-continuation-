# EMA Hourly Continuation — NOT/USDT P8_100

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6518 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -3.4292 |
| sortino_ratio | -1.1274 |
| max_drawdown | 0.7463 |
| cagr | -0.4202 |
| net_avg_win | 53.6675 |
| net_avg_loss | -76.6528 |
| avg_hold_time_bars | 29.4049 |
| exposure | 0.7335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
