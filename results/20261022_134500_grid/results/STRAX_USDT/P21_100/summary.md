# EMA Hourly Continuation — STRAX/USDT P21_100

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.5387 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.8005 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -6.7812 |
| sortino_ratio | -2.6130 |
| max_drawdown | 0.9602 |
| cagr | -0.7217 |
| net_avg_win | 36.1255 |
| net_avg_loss | -47.1401 |
| avg_hold_time_bars | 11.7510 |
| exposure | 0.4035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
