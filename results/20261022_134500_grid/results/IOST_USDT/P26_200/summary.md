# EMA Hourly Continuation — IOST/USDT P26_200

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7593 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.1590 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | -1.6299 |
| sortino_ratio | -0.4391 |
| max_drawdown | 0.4878 |
| cagr | -0.1936 |
| net_avg_win | 67.5326 |
| net_avg_loss | -98.5391 |
| avg_hold_time_bars | 34.4609 |
| exposure | 0.5811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
