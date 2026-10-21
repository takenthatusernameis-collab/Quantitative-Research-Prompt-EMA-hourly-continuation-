# EMA Hourly Continuation — BNB/USDT P34_50

**Symbol:** BNB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 0.4476 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8587 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.4357 |
| sortino_ratio | -0.7217 |
| max_drawdown | 0.5716 |
| cagr | -0.2818 |
| net_avg_win | 47.1515 |
| net_avg_loss | -91.2378 |
| avg_hold_time_bars | 5.7081 |
| exposure | 0.0542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
