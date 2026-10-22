# EMA Hourly Continuation — WAVES/USDT P8_12

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -3.4354 |
| sortino_ratio | -0.8636 |
| max_drawdown | 0.6553 |
| cagr | -0.3299 |
| net_avg_win | 58.1471 |
| net_avg_loss | -86.7148 |
| avg_hold_time_bars | 4.8306 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
