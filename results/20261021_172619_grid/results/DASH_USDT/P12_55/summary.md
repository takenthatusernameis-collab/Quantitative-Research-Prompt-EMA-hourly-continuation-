# EMA Hourly Continuation — DASH/USDT P12_55

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.7281 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.2895 |
| sortino_ratio | -0.8053 |
| max_drawdown | 0.6149 |
| cagr | -0.3091 |
| net_avg_win | 54.3554 |
| net_avg_loss | -72.7002 |
| avg_hold_time_bars | 12.1457 |
| exposure | 0.3335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
