# EMA Hourly Continuation — CETUS/USDT P50_144

**Symbol:** CETUS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.5153 |
| gross_profit_factor | 1.0846 |
| gross_win_rate | 0.5215 |
| sharpe_ratio | -2.0877 |
| sortino_ratio | -0.6505 |
| max_drawdown | 0.5568 |
| cagr | -0.2682 |
| net_avg_win | 65.5544 |
| net_avg_loss | -92.7036 |
| avg_hold_time_bars | 13.6094 |
| exposure | 0.3012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
