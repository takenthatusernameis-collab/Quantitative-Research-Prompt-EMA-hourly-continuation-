# EMA Hourly Continuation — POLYX/USDT P26_50

**Symbol:** POLYX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.5395 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -6.9351 |
| sortino_ratio | -2.9592 |
| max_drawdown | 0.9746 |
| cagr | -0.7628 |
| net_avg_win | 27.3391 |
| net_avg_loss | -43.0364 |
| avg_hold_time_bars | 4.1090 |
| exposure | 0.1696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
