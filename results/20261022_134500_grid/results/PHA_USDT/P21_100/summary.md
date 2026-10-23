# EMA Hourly Continuation — PHA/USDT P21_100

**Symbol:** PHA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5570 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -4.4312 |
| sortino_ratio | -1.6252 |
| max_drawdown | 0.8674 |
| cagr | -0.5451 |
| net_avg_win | 35.0670 |
| net_avg_loss | -51.3258 |
| avg_hold_time_bars | 12.7863 |
| exposure | 0.3999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
