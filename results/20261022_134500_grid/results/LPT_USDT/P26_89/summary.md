# EMA Hourly Continuation — LPT/USDT P26_89

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.5257 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -5.6503 |
| sortino_ratio | -2.2113 |
| max_drawdown | 0.9344 |
| cagr | -0.6539 |
| net_avg_win | 30.1478 |
| net_avg_loss | -44.9873 |
| avg_hold_time_bars | 8.6375 |
| exposure | 0.3055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
