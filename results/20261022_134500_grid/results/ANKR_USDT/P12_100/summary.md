# EMA Hourly Continuation — ANKR/USDT P12_100

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -3.5373 |
| sortino_ratio | -1.1563 |
| max_drawdown | 0.7656 |
| cagr | -0.4284 |
| net_avg_win | 49.9665 |
| net_avg_loss | -72.4895 |
| avg_hold_time_bars | 26.3119 |
| exposure | 0.6518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
