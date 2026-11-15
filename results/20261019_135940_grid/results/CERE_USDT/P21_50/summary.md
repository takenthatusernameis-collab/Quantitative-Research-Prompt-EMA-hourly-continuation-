# EMA Hourly Continuation — CERE/USDT P21_50

**Symbol:** CERE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.3600 |
| net_win_rate | 0.3187 |
| gross_profit_factor | 0.7088 |
| gross_win_rate | 0.3646 |
| sharpe_ratio | -13.6453 |
| sortino_ratio | -6.3384 |
| max_drawdown | 0.9998 |
| cagr | -0.9651 |
| net_avg_win | 16.8907 |
| net_avg_loss | -21.9416 |
| avg_hold_time_bars | 5.6967 |
| exposure | 0.2706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
