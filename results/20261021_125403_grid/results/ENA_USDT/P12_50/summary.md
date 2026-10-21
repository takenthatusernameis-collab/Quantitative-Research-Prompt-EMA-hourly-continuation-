# EMA Hourly Continuation — ENA/USDT P12_50

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.9374 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1096 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.4465 |
| sortino_ratio | -0.1581 |
| max_drawdown | 0.3400 |
| cagr | -0.0779 |
| net_avg_win | 86.7983 |
| net_avg_loss | -103.6760 |
| avg_hold_time_bars | 11.0997 |
| exposure | 0.3037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
