# EMA Hourly Continuation — METIS/USDT P55_200

**Symbol:** METIS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6860 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8184 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -2.1071 |
| sortino_ratio | -0.5246 |
| max_drawdown | 0.4647 |
| cagr | -0.2152 |
| net_avg_win | 71.6517 |
| net_avg_loss | -85.3990 |
| avg_hold_time_bars | 25.6602 |
| exposure | 0.3604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
