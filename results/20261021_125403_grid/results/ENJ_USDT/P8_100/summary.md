# EMA Hourly Continuation — ENJ/USDT P8_100

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.8110 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.4889 |
| sortino_ratio | -0.4654 |
| max_drawdown | 0.4833 |
| cagr | -0.1945 |
| net_avg_win | 75.7895 |
| net_avg_loss | -91.5346 |
| avg_hold_time_bars | 30.4283 |
| exposure | 0.6623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
