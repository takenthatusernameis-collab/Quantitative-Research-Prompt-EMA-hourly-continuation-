# EMA Hourly Continuation — BOME/USDT P34_200

**Symbol:** BOME/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.9776 |
| net_win_rate | 0.5347 |
| gross_profit_factor | 1.1371 |
| gross_win_rate | 0.5347 |
| sharpe_ratio | -0.0588 |
| sortino_ratio | -0.0144 |
| max_drawdown | 0.2159 |
| cagr | -0.0119 |
| net_avg_win | 83.9980 |
| net_avg_loss | -98.7504 |
| avg_hold_time_bars | 39.2569 |
| exposure | 0.5139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
