# EMA Hourly Continuation — ID/USDT P26_89

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5975 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -3.6646 |
| sortino_ratio | -1.3310 |
| max_drawdown | 0.8033 |
| cagr | -0.4674 |
| net_avg_win | 36.8023 |
| net_avg_loss | -57.1464 |
| avg_hold_time_bars | 11.0750 |
| exposure | 0.3343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
