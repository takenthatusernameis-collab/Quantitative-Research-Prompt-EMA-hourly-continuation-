# EMA Hourly Continuation — SHIB/USDT P50_55

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.7239 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0705 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -0.9188 |
| sortino_ratio | -0.1222 |
| max_drawdown | 0.1758 |
| cagr | -0.0542 |
| net_avg_win | 77.8729 |
| net_avg_loss | -115.4435 |
| avg_hold_time_bars | 6.7765 |
| exposure | 0.0262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
