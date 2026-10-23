# EMA Hourly Continuation — CSPR/USDT P12_200

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8115 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -4.8707 |
| sortino_ratio | -1.7521 |
| max_drawdown | 0.8764 |
| cagr | -0.5630 |
| net_avg_win | 41.2431 |
| net_avg_loss | -54.5275 |
| avg_hold_time_bars | 22.5352 |
| exposure | 0.6699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
