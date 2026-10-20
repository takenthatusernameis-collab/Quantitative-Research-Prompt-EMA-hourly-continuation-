# EMA Hourly Continuation — NMR/USDT P100_200

**Symbol:** NMR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.4794 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.8508 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -4.9149 |
| sortino_ratio | -1.4096 |
| max_drawdown | 0.8366 |
| cagr | -0.5093 |
| net_avg_win | 42.1319 |
| net_avg_loss | -66.3668 |
| avg_hold_time_bars | 9.7305 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
