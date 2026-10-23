# EMA Hourly Continuation — LUNA/USDT P8_100

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 855 |
| net_profit_factor | 0.5466 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.9123 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -6.2889 |
| sortino_ratio | -2.5633 |
| max_drawdown | 0.9612 |
| cagr | -0.7234 |
| net_avg_win | 30.1462 |
| net_avg_loss | -44.9673 |
| avg_hold_time_bars | 15.5532 |
| exposure | 0.6045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
