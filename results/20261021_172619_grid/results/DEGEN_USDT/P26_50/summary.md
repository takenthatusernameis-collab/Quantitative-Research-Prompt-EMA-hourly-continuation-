# EMA Hourly Continuation — DEGEN/USDT P26_50

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.7842 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9921 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.6614 |
| sortino_ratio | -0.4794 |
| max_drawdown | 0.4421 |
| cagr | -0.1982 |
| net_avg_win | 76.8568 |
| net_avg_loss | -96.0988 |
| avg_hold_time_bars | 6.1650 |
| exposure | 0.1140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
