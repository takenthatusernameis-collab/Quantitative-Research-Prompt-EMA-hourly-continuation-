# EMA Hourly Continuation — CTSI/USDT P8_34

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1302 |
| net_profit_factor | 0.6030 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 1.0920 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -6.7430 |
| sortino_ratio | -3.4469 |
| max_drawdown | 0.9838 |
| cagr | -0.8048 |
| net_avg_win | 24.1335 |
| net_avg_loss | -36.2715 |
| avg_hold_time_bars | 6.1575 |
| exposure | 0.3644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
