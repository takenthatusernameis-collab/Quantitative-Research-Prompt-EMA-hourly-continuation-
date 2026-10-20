# EMA Hourly Continuation — ORCA/USDT P21_55

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9379 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -5.3950 |
| sortino_ratio | -2.1938 |
| max_drawdown | 0.9381 |
| cagr | -0.6615 |
| net_avg_win | 30.7041 |
| net_avg_loss | -49.0186 |
| avg_hold_time_bars | 6.5366 |
| exposure | 0.2514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
