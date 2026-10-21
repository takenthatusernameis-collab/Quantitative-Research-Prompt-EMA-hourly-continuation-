# EMA Hourly Continuation — ENJ/USDT P26_50

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7528 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0606 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.9978 |
| sortino_ratio | -0.6056 |
| max_drawdown | 0.5516 |
| cagr | -0.2422 |
| net_avg_win | 67.2177 |
| net_avg_loss | -92.9571 |
| avg_hold_time_bars | 5.8009 |
| exposure | 0.1173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
