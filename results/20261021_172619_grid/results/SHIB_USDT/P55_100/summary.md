# EMA Hourly Continuation — SHIB/USDT P55_100

**Symbol:** SHIB/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.6868 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -2.2426 |
| sortino_ratio | -0.5713 |
| max_drawdown | 0.4900 |
| cagr | -0.2298 |
| net_avg_win | 68.9233 |
| net_avg_loss | -94.2008 |
| avg_hold_time_bars | 7.7975 |
| exposure | 0.1120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
