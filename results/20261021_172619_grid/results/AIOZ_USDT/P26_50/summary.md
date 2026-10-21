# EMA Hourly Continuation — AIOZ/USDT P26_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7521 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9605 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.8053 |
| sortino_ratio | -0.5007 |
| max_drawdown | 0.4724 |
| cagr | -0.2052 |
| net_avg_win | 72.2403 |
| net_avg_loss | -92.0539 |
| avg_hold_time_bars | 6.9947 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
