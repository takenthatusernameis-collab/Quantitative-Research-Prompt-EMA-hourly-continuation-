# EMA Hourly Continuation — NOT/USDT P8_55

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.6400 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -5.3266 |
| sortino_ratio | -2.4770 |
| max_drawdown | 0.9490 |
| cagr | -0.6974 |
| net_avg_win | 33.0122 |
| net_avg_loss | -47.7374 |
| avg_hold_time_bars | 9.5345 |
| exposure | 0.4743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
