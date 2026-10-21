# EMA Hourly Continuation — SUN/USDT P89_100

**Symbol:** SUN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.2408 |
| net_win_rate | 0.2913 |
| gross_profit_factor | 0.6337 |
| gross_win_rate | 0.3544 |
| sharpe_ratio | -6.5048 |
| sortino_ratio | -1.3968 |
| max_drawdown | 0.8324 |
| cagr | -0.5032 |
| net_avg_win | 43.8009 |
| net_avg_loss | -74.7658 |
| avg_hold_time_bars | 5.5583 |
| exposure | 0.0518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
