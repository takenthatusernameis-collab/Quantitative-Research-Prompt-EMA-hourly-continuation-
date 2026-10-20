# EMA Hourly Continuation — METIS/USDT P12_100

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -4.8724 |
| sortino_ratio | -1.7251 |
| max_drawdown | 0.8812 |
| cagr | -0.5635 |
| net_avg_win | 46.0211 |
| net_avg_loss | -60.6123 |
| avg_hold_time_bars | 20.5542 |
| exposure | 0.5951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
