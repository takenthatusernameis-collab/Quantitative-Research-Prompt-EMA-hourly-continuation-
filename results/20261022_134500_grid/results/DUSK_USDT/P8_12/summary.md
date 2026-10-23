# EMA Hourly Continuation — DUSK/USDT P8_12

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1799 |
| net_profit_factor | 0.2936 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -14.8227 |
| sortino_ratio | -8.9563 |
| max_drawdown | 1.0000 |
| cagr | -0.9901 |
| net_avg_win | 5.7956 |
| net_avg_loss | -13.0826 |
| avg_hold_time_bars | 2.0306 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
