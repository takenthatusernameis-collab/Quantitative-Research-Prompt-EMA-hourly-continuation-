# EMA Hourly Continuation — EWT/USDT P8_21

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.5642 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.7845 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -3.7847 |
| sortino_ratio | -1.1145 |
| max_drawdown | 0.7585 |
| cagr | -0.4030 |
| net_avg_win | 50.0001 |
| net_avg_loss | -69.1357 |
| avg_hold_time_bars | 7.1189 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
