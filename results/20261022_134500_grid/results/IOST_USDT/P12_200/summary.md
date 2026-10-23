# EMA Hourly Continuation — IOST/USDT P12_200

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7269 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0988 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -1.7628 |
| sortino_ratio | -0.4633 |
| max_drawdown | 0.4714 |
| cagr | -0.2010 |
| net_avg_win | 63.6877 |
| net_avg_loss | -92.2293 |
| avg_hold_time_bars | 47.8803 |
| exposure | 0.7639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
