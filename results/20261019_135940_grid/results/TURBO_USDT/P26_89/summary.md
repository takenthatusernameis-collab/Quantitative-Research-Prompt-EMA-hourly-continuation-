# EMA Hourly Continuation — TURBO/USDT P26_89

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6441 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -4.0480 |
| sortino_ratio | -1.5722 |
| max_drawdown | 0.7970 |
| cagr | -0.5237 |
| net_avg_win | 47.5391 |
| net_avg_loss | -66.8990 |
| avg_hold_time_bars | 8.6593 |
| exposure | 0.2981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
