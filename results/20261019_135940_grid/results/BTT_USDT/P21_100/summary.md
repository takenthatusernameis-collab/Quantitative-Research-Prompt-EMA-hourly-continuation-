# EMA Hourly Continuation — BTT/USDT P21_100

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.3790 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -9.0420 |
| sortino_ratio | -3.1894 |
| max_drawdown | 0.9855 |
| cagr | -0.8145 |
| net_avg_win | 26.2664 |
| net_avg_loss | -41.6523 |
| avg_hold_time_bars | 16.9213 |
| exposure | 0.4692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
