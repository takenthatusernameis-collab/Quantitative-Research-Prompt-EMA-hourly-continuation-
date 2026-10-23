# EMA Hourly Continuation — SWFTC/USDT P55_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5239 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -5.5295 |
| sortino_ratio | -1.8414 |
| max_drawdown | 0.8986 |
| cagr | -0.5941 |
| net_avg_win | 41.0821 |
| net_avg_loss | -59.1840 |
| avg_hold_time_bars | 8.3513 |
| exposure | 0.2118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
