# EMA Hourly Continuation — BIGTIME/USDT P26_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6977 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0119 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -3.1499 |
| sortino_ratio | -1.1347 |
| max_drawdown | 0.7728 |
| cagr | -0.4178 |
| net_avg_win | 53.0431 |
| net_avg_loss | -73.9683 |
| avg_hold_time_bars | 11.6651 |
| exposure | 0.3468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
