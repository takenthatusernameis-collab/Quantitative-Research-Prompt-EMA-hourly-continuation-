# EMA Hourly Continuation — BLUR/USDT P55_89

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.5674 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 1.0334 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -5.1662 |
| sortino_ratio | -1.8390 |
| max_drawdown | 0.9011 |
| cagr | -0.5896 |
| net_avg_win | 39.2274 |
| net_avg_loss | -61.1574 |
| avg_hold_time_bars | 4.3752 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
