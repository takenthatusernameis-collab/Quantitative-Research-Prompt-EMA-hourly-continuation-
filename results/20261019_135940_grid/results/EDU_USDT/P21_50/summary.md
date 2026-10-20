# EMA Hourly Continuation — EDU/USDT P21_50

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1037 |
| net_profit_factor | 0.4573 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.7663 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -7.0241 |
| sortino_ratio | -3.1824 |
| max_drawdown | 0.9804 |
| cagr | -0.7838 |
| net_avg_win | 17.8192 |
| net_avg_loss | -31.4290 |
| avg_hold_time_bars | 4.7994 |
| exposure | 0.2252 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
