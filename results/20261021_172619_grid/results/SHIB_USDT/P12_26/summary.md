# EMA Hourly Continuation — SHIB/USDT P12_26

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0088 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -2.2982 |
| sortino_ratio | -0.6474 |
| max_drawdown | 0.5240 |
| cagr | -0.2554 |
| net_avg_win | 62.3040 |
| net_avg_loss | -90.0251 |
| avg_hold_time_bars | 5.4961 |
| exposure | 0.0957 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
