# EMA Hourly Continuation — ANKR/USDT P12_100

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7695 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.8396 |
| sortino_ratio | -0.5449 |
| max_drawdown | 0.5208 |
| cagr | -0.2231 |
| net_avg_win | 73.5857 |
| net_avg_loss | -93.4374 |
| avg_hold_time_bars | 32.7425 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
