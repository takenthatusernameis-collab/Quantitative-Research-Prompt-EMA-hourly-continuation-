# EMA Hourly Continuation — MLK/USDT P21_89

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.3272 |
| net_win_rate | 0.3052 |
| gross_profit_factor | 0.5877 |
| gross_win_rate | 0.3120 |
| sharpe_ratio | -12.6062 |
| sortino_ratio | -5.7519 |
| max_drawdown | 0.9993 |
| cagr | -0.9440 |
| net_avg_win | 15.4808 |
| net_avg_loss | -20.7748 |
| avg_hold_time_bars | 7.5219 |
| exposure | 0.3503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
