# EMA Hourly Continuation — IOST/USDT P8_21

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1563 |
| net_profit_factor | 0.3795 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -11.1837 |
| sortino_ratio | -6.2687 |
| max_drawdown | 0.9996 |
| cagr | -0.9567 |
| net_avg_win | 8.7716 |
| net_avg_loss | -18.6028 |
| avg_hold_time_bars | 3.6667 |
| exposure | 0.2605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
