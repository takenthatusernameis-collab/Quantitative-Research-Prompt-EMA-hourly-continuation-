# EMA Hourly Continuation — METIS/USDT P12_50

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.5172 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8395 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -6.5044 |
| sortino_ratio | -2.9045 |
| max_drawdown | 0.9727 |
| cagr | -0.7551 |
| net_avg_win | 22.8066 |
| net_avg_loss | -36.2302 |
| avg_hold_time_bars | 8.4491 |
| exposure | 0.3883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
