# EMA Hourly Continuation — OP/USDT P100_200

**Symbol:** OP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6840 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0713 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.5208 |
| sortino_ratio | -0.7080 |
| max_drawdown | 0.6001 |
| cagr | -0.2857 |
| net_avg_win | 62.9982 |
| net_avg_loss | -92.1024 |
| avg_hold_time_bars | 8.8929 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
