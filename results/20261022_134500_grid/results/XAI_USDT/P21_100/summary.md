# EMA Hourly Continuation — XAI/USDT P21_100

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.6911 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -4.3493 |
| sortino_ratio | -1.6249 |
| max_drawdown | 0.8825 |
| cagr | -0.5359 |
| net_avg_win | 60.1330 |
| net_avg_loss | -72.6181 |
| avg_hold_time_bars | 14.3934 |
| exposure | 0.4573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
