# EMA Hourly Continuation — BTT/USDT P20_34

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.1537 |
| net_win_rate | 0.2694 |
| gross_profit_factor | 0.5454 |
| gross_win_rate | 0.3598 |
| sharpe_ratio | -18.5427 |
| sortino_ratio | -9.8145 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 5.6934 |
| net_avg_loss | -13.6603 |
| avg_hold_time_bars | 2.9992 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
