# EMA Hourly Continuation — XPR/USDT P12_21

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1343 |
| net_profit_factor | 0.2465 |
| net_win_rate | 0.3299 |
| gross_profit_factor | 0.6635 |
| gross_win_rate | 0.3589 |
| sharpe_ratio | -16.8614 |
| sortino_ratio | -9.0769 |
| max_drawdown | 1.0000 |
| cagr | -0.9931 |
| net_avg_win | 7.3832 |
| net_avg_loss | -14.7452 |
| avg_hold_time_bars | 2.2599 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
