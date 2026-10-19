# EMA Hourly Continuation — TWT/USDT P50_100

**Symbol:** TWT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.4088 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -6.8550 |
| sortino_ratio | -2.5006 |
| max_drawdown | 0.9567 |
| cagr | -0.7083 |
| net_avg_win | 22.9244 |
| net_avg_loss | -43.2945 |
| avg_hold_time_bars | 5.9834 |
| exposure | 0.1798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
