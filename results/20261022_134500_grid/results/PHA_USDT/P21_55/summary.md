# EMA Hourly Continuation — PHA/USDT P21_55

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.5223 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8718 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -6.2088 |
| sortino_ratio | -2.7036 |
| max_drawdown | 0.9632 |
| cagr | -0.7298 |
| net_avg_win | 24.1978 |
| net_avg_loss | -38.5318 |
| avg_hold_time_bars | 5.3873 |
| exposure | 0.2346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
