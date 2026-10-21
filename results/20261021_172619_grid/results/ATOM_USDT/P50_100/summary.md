# EMA Hourly Continuation — ATOM/USDT P50_100

**Symbol:** ATOM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9807 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.6372 |
| sortino_ratio | -0.4143 |
| max_drawdown | 0.4239 |
| cagr | -0.1724 |
| net_avg_win | 61.4372 |
| net_avg_loss | -86.7978 |
| avg_hold_time_bars | 9.0903 |
| exposure | 0.1281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
