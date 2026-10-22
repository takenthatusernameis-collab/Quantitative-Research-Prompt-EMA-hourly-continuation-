# EMA Hourly Continuation — PIXEL/USDT P26_50

**Symbol:** PIXEL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.5845 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -5.6119 |
| sortino_ratio | -2.4183 |
| max_drawdown | 0.9531 |
| cagr | -0.6908 |
| net_avg_win | 29.5058 |
| net_avg_loss | -47.1461 |
| avg_hold_time_bars | 4.3216 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
