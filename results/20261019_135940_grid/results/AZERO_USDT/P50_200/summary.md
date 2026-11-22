# EMA Hourly Continuation — AZERO/USDT P50_200

**Symbol:** AZERO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.7400 |
| sortino_ratio | -0.4593 |
| max_drawdown | 0.4989 |
| cagr | -0.2011 |
| net_avg_win | 69.5754 |
| net_avg_loss | -92.3117 |
| avg_hold_time_bars | 24.4345 |
| exposure | 0.3969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
