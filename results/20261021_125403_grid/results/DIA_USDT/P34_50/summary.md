# EMA Hourly Continuation — DIA/USDT P34_50

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.4894 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.7062 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -4.0358 |
| sortino_ratio | -1.0539 |
| max_drawdown | 0.7201 |
| cagr | -0.3854 |
| net_avg_win | 48.4208 |
| net_avg_loss | -70.3070 |
| avg_hold_time_bars | 5.8754 |
| exposure | 0.0896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
