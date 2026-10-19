# EMA Hourly Continuation — DCR/USDT P21_100

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -5.0935 |
| sortino_ratio | -1.9526 |
| max_drawdown | 0.9151 |
| cagr | -0.6131 |
| net_avg_win | 28.8094 |
| net_avg_loss | -47.0532 |
| avg_hold_time_bars | 11.6911 |
| exposure | 0.3973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
