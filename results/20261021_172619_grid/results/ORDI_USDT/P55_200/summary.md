# EMA Hourly Continuation — ORDI/USDT P55_200

**Symbol:** ORDI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7561 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -1.4882 |
| sortino_ratio | -0.3687 |
| max_drawdown | 0.3863 |
| cagr | -0.1562 |
| net_avg_win | 74.7652 |
| net_avg_loss | -89.5551 |
| avg_hold_time_bars | 23.2409 |
| exposure | 0.3201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
