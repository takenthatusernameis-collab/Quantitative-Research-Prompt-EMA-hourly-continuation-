# EMA Hourly Continuation — SYN/USDT P8_50

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.6199 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -5.5228 |
| sortino_ratio | -2.5465 |
| max_drawdown | 0.9558 |
| cagr | -0.7108 |
| net_avg_win | 30.7389 |
| net_avg_loss | -43.1235 |
| avg_hold_time_bars | 9.3239 |
| exposure | 0.4620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
