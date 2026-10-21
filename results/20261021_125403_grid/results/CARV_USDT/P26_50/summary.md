# EMA Hourly Continuation — CARV/USDT P26_50

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.5886 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8405 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.6074 |
| sortino_ratio | -1.1385 |
| max_drawdown | 0.6611 |
| cagr | -0.4061 |
| net_avg_win | 51.8539 |
| net_avg_loss | -73.7588 |
| avg_hold_time_bars | 7.2354 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
