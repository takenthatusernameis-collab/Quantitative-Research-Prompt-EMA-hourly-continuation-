# EMA Hourly Continuation — RLC/USDT P50_200

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6505 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9012 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.4928 |
| sortino_ratio | -0.6844 |
| max_drawdown | 0.5632 |
| cagr | -0.2729 |
| net_avg_win | 57.6061 |
| net_avg_loss | -79.6060 |
| avg_hold_time_bars | 24.8963 |
| exposure | 0.4255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
