# EMA Hourly Continuation — ONDO/USDT P21_26

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.7045 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9471 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.2372 |
| sortino_ratio | -0.1924 |
| max_drawdown | 0.2649 |
| cagr | -0.0844 |
| net_avg_win | 83.1432 |
| net_avg_loss | -110.2707 |
| avg_hold_time_bars | 5.0424 |
| exposure | 0.0270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
