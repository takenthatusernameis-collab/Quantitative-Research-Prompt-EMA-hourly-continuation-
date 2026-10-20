# EMA Hourly Continuation — SKL/USDT P55_100

**Symbol:** SKL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5726 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9392 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -4.1271 |
| sortino_ratio | -1.4743 |
| max_drawdown | 0.8318 |
| cagr | -0.5012 |
| net_avg_win | 36.0271 |
| net_avg_loss | -59.4364 |
| avg_hold_time_bars | 5.5316 |
| exposure | 0.1589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
