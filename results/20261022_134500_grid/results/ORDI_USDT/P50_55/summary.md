# EMA Hourly Continuation — ORDI/USDT P50_55

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.2553 |
| net_win_rate | 0.3773 |
| gross_profit_factor | 0.7100 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -11.2473 |
| sortino_ratio | -4.7532 |
| max_drawdown | 0.9982 |
| cagr | -0.9191 |
| net_avg_win | 10.5967 |
| net_avg_loss | -25.1494 |
| avg_hold_time_bars | 1.8610 |
| exposure | 0.0724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
