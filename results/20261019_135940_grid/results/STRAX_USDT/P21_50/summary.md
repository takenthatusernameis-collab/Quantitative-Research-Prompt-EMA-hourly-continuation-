# EMA Hourly Continuation — STRAX/USDT P21_50

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.4869 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.8504 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -8.6107 |
| sortino_ratio | -3.7835 |
| max_drawdown | 0.9917 |
| cagr | -0.8523 |
| net_avg_win | 23.0070 |
| net_avg_loss | -34.1440 |
| avg_hold_time_bars | 6.3938 |
| exposure | 0.2850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
