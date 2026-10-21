# EMA Hourly Continuation — LSK/USDT P8_144

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.9207 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.1360 |
| gross_win_rate | 0.5345 |
| sharpe_ratio | -0.4836 |
| sortino_ratio | -0.1378 |
| max_drawdown | 0.3313 |
| cagr | -0.0662 |
| net_avg_win | 87.7813 |
| net_avg_loss | -109.4884 |
| avg_hold_time_bars | 41.3171 |
| exposure | 0.7343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
