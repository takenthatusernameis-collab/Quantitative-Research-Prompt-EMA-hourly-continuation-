# EMA Hourly Continuation — AGLD/USDT P34_200

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7268 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.2511 |
| sortino_ratio | -0.6286 |
| max_drawdown | 0.5840 |
| cagr | -0.2569 |
| net_avg_win | 74.5926 |
| net_avg_loss | -93.2092 |
| avg_hold_time_bars | 29.4835 |
| exposure | 0.5270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
