# EMA Hourly Continuation — JTO/USDT P26_89

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.6384 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9207 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.1293 |
| sortino_ratio | -1.5366 |
| max_drawdown | 0.8516 |
| cagr | -0.5180 |
| net_avg_win | 45.9069 |
| net_avg_loss | -61.4495 |
| avg_hold_time_bars | 9.5078 |
| exposure | 0.3030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
