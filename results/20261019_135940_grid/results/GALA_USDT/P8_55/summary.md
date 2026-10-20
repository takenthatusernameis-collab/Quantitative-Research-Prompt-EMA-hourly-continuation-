# EMA Hourly Continuation — GALA/USDT P8_55

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1033 |
| net_profit_factor | 0.4952 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.7827 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -6.7492 |
| sortino_ratio | -3.0455 |
| max_drawdown | 0.9771 |
| cagr | -0.7726 |
| net_avg_win | 20.9897 |
| net_avg_loss | -33.4990 |
| avg_hold_time_bars | 10.5363 |
| exposure | 0.4947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
