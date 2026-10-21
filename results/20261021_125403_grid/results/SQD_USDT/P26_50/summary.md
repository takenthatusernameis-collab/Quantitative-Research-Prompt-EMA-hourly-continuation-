# EMA Hourly Continuation — SQD/USDT P26_50

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.8327 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0459 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.2947 |
| sortino_ratio | -0.3840 |
| max_drawdown | 0.4333 |
| cagr | -0.1631 |
| net_avg_win | 83.1915 |
| net_avg_loss | -103.3537 |
| avg_hold_time_bars | 6.6223 |
| exposure | 0.1286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
