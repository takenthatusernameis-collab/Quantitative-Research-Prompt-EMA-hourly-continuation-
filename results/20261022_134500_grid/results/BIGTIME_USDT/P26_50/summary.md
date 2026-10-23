# EMA Hourly Continuation — BIGTIME/USDT P26_50

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -5.8267 |
| sortino_ratio | -2.5123 |
| max_drawdown | 0.9516 |
| cagr | -0.6990 |
| net_avg_win | 28.6628 |
| net_avg_loss | -45.6723 |
| avg_hold_time_bars | 4.4898 |
| exposure | 0.1892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
