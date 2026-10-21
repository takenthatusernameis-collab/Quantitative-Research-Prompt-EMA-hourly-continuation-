# EMA Hourly Continuation — ORDI/USDT P50_100

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7543 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9581 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.6683 |
| sortino_ratio | -0.4452 |
| max_drawdown | 0.4399 |
| cagr | -0.1844 |
| net_avg_win | 72.3475 |
| net_avg_loss | -91.6077 |
| avg_hold_time_bars | 9.8822 |
| exposure | 0.1563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
