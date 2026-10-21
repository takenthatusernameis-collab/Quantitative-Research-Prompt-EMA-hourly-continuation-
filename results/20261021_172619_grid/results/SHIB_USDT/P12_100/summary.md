# EMA Hourly Continuation — SHIB/USDT P12_100

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.8136 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.5949 |
| sortino_ratio | -0.5229 |
| max_drawdown | 0.5015 |
| cagr | -0.2147 |
| net_avg_win | 75.2178 |
| net_avg_loss | -94.2372 |
| avg_hold_time_bars | 21.0038 |
| exposure | 0.4993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
