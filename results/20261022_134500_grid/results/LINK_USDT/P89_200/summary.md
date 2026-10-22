# EMA Hourly Continuation — LINK/USDT P89_200

**Symbol:** LINK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.5625 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9372 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -3.5279 |
| sortino_ratio | -0.9789 |
| max_drawdown | 0.7040 |
| cagr | -0.3740 |
| net_avg_win | 48.8591 |
| net_avg_loss | -76.7403 |
| avg_hold_time_bars | 10.2655 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
