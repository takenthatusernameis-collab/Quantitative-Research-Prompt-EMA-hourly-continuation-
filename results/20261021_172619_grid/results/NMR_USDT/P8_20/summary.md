# EMA Hourly Continuation — NMR/USDT P8_20

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6489 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -3.9157 |
| sortino_ratio | -1.4444 |
| max_drawdown | 0.8264 |
| cagr | -0.4855 |
| net_avg_win | 47.3240 |
| net_avg_loss | -66.6202 |
| avg_hold_time_bars | 4.8524 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
