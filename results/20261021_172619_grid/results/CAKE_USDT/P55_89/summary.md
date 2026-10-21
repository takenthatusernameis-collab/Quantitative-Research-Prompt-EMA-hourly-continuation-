# EMA Hourly Continuation — CAKE/USDT P55_89

**Symbol:** CAKE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7749 |
| net_win_rate | 0.5318 |
| gross_profit_factor | 1.1346 |
| gross_win_rate | 0.5318 |
| sharpe_ratio | -1.3724 |
| sortino_ratio | -0.3430 |
| max_drawdown | 0.3664 |
| cagr | -0.1453 |
| net_avg_win | 70.5392 |
| net_avg_loss | -103.3849 |
| avg_hold_time_bars | 7.7324 |
| exposure | 0.1051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
