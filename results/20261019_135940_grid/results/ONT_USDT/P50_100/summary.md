# EMA Hourly Continuation — ONT/USDT P50_100

**Symbol:** ONT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.4791 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7742 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -5.1721 |
| sortino_ratio | -1.8218 |
| max_drawdown | 0.8893 |
| cagr | -0.5754 |
| net_avg_win | 29.8102 |
| net_avg_loss | -49.0931 |
| avg_hold_time_bars | 6.9871 |
| exposure | 0.1957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
