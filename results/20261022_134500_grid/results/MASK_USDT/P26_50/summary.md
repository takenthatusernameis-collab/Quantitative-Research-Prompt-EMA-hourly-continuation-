# EMA Hourly Continuation — MASK/USDT P26_50

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.3707 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.8525 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -8.8324 |
| sortino_ratio | -3.9085 |
| max_drawdown | 0.9930 |
| cagr | -0.8601 |
| net_avg_win | 13.6672 |
| net_avg_loss | -28.8974 |
| avg_hold_time_bars | 3.9240 |
| exposure | 0.1737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
