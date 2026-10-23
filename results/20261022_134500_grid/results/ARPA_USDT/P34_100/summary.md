# EMA Hourly Continuation — ARPA/USDT P34_100

**Symbol:** ARPA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.4873 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -6.4213 |
| sortino_ratio | -2.4124 |
| max_drawdown | 0.9491 |
| cagr | -0.6886 |
| net_avg_win | 29.7181 |
| net_avg_loss | -44.9580 |
| avg_hold_time_bars | 9.0406 |
| exposure | 0.2921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
