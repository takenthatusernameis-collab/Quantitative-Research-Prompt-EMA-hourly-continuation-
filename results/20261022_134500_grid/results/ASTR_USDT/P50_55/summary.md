# EMA Hourly Continuation — ASTR/USDT P50_55

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.2235 |
| net_win_rate | 0.3564 |
| gross_profit_factor | 0.8705 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -11.5754 |
| sortino_ratio | -4.6879 |
| max_drawdown | 0.9982 |
| cagr | -0.9187 |
| net_avg_win | 10.7221 |
| net_avg_loss | -26.5614 |
| avg_hold_time_bars | 2.3670 |
| exposure | 0.0806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
