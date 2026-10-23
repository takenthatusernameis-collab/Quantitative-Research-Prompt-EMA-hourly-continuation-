# EMA Hourly Continuation — RSR/USDT P89_100

**Symbol:** RSR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.3644 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 0.8822 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -7.5409 |
| sortino_ratio | -2.6705 |
| max_drawdown | 0.9664 |
| cagr | -0.7404 |
| net_avg_win | 21.0667 |
| net_avg_loss | -43.1889 |
| avg_hold_time_bars | 2.1041 |
| exposure | 0.0588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
