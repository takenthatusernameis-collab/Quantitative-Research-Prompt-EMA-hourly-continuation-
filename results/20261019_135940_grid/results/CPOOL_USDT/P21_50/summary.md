# EMA Hourly Continuation — CPOOL/USDT P21_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.5494 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8150 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -6.2707 |
| sortino_ratio | -2.7354 |
| max_drawdown | 0.9685 |
| cagr | -0.7456 |
| net_avg_win | 26.2831 |
| net_avg_loss | -39.9993 |
| avg_hold_time_bars | 4.3377 |
| exposure | 0.1944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
