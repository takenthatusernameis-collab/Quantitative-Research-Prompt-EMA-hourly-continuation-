# EMA Hourly Continuation — POLYX/USDT P20_100

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.6688 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.3856 |
| sortino_ratio | -1.1992 |
| max_drawdown | 0.7737 |
| cagr | -0.4333 |
| net_avg_win | 50.2977 |
| net_avg_loss | -70.5814 |
| avg_hold_time_bars | 14.7492 |
| exposure | 0.4224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
