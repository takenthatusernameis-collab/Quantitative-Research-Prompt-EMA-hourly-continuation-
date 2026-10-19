# EMA Hourly Continuation — CFX/USDT P26_50

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.4150 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.7706 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -8.7842 |
| sortino_ratio | -3.8549 |
| max_drawdown | 0.9923 |
| cagr | -0.8550 |
| net_avg_win | 17.0859 |
| net_avg_loss | -30.3419 |
| avg_hold_time_bars | 3.7703 |
| exposure | 0.1664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
