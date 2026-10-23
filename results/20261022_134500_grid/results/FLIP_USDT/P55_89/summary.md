# EMA Hourly Continuation — FLIP/USDT P55_89

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.3883 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.7892 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -6.9998 |
| sortino_ratio | -2.0933 |
| max_drawdown | 0.9331 |
| cagr | -0.6557 |
| net_avg_win | 34.7770 |
| net_avg_loss | -54.9628 |
| avg_hold_time_bars | 8.0649 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
