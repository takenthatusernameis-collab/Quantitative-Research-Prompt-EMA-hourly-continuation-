# EMA Hourly Continuation — PHA/USDT P12_55

**Symbol:** PHA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.6180 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -4.8294 |
| sortino_ratio | -2.1489 |
| max_drawdown | 0.9268 |
| cagr | -0.6442 |
| net_avg_win | 31.0646 |
| net_avg_loss | -46.6801 |
| avg_hold_time_bars | 8.3716 |
| exposure | 0.3809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
