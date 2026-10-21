# EMA Hourly Continuation — ASTR/USDT P8_100

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9501 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.0060 |
| sortino_ratio | -0.6224 |
| max_drawdown | 0.5381 |
| cagr | -0.2496 |
| net_avg_win | 66.5017 |
| net_avg_loss | -84.3496 |
| avg_hold_time_bars | 31.3214 |
| exposure | 0.6747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
