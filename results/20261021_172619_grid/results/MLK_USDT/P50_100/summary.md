# EMA Hourly Continuation — MLK/USDT P50_100

**Symbol:** MLK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.3451 |
| net_win_rate | 0.3246 |
| gross_profit_factor | 0.5063 |
| gross_win_rate | 0.3275 |
| sharpe_ratio | -5.9813 |
| sortino_ratio | -1.5650 |
| max_drawdown | 0.8459 |
| cagr | -0.5218 |
| net_avg_win | 40.0931 |
| net_avg_loss | -55.8229 |
| avg_hold_time_bars | 9.4444 |
| exposure | 0.1462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
