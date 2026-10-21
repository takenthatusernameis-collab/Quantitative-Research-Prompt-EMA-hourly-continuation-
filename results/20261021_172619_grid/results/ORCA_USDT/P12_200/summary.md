# EMA Hourly Continuation — ORCA/USDT P12_200

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7458 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -1.5391 |
| sortino_ratio | -0.3834 |
| max_drawdown | 0.4036 |
| cagr | -0.1633 |
| net_avg_win | 71.5681 |
| net_avg_loss | -89.3189 |
| avg_hold_time_bars | 53.8795 |
| exposure | 0.7519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
