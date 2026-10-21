# EMA Hourly Continuation — CELO/USDT P26_50

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -2.7850 |
| sortino_ratio | -0.8701 |
| max_drawdown | 0.6369 |
| cagr | -0.3277 |
| net_avg_win | 54.7758 |
| net_avg_loss | -76.8454 |
| avg_hold_time_bars | 6.2845 |
| exposure | 0.1359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
