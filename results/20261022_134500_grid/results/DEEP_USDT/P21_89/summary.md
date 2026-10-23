# EMA Hourly Continuation — DEEP/USDT P21_89

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7146 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9581 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.7469 |
| sortino_ratio | -0.9729 |
| max_drawdown | 0.6034 |
| cagr | -0.3665 |
| net_avg_win | 61.4880 |
| net_avg_loss | -82.3480 |
| avg_hold_time_bars | 14.0140 |
| exposure | 0.3975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
