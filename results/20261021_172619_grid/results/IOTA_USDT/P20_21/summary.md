# EMA Hourly Continuation — IOTA/USDT P20_21

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.6525 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -1.8842 |
| sortino_ratio | -0.3602 |
| max_drawdown | 0.3840 |
| cagr | -0.1513 |
| net_avg_win | 73.6904 |
| net_avg_loss | -106.7382 |
| avg_hold_time_bars | 4.2203 |
| exposure | 0.0340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
