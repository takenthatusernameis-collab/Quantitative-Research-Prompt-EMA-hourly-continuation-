# EMA Hourly Continuation — CTC/USDT P50_89

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.3630 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7379 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -7.4902 |
| sortino_ratio | -2.7510 |
| max_drawdown | 0.9679 |
| cagr | -0.7440 |
| net_avg_win | 19.8973 |
| net_avg_loss | -38.7377 |
| avg_hold_time_bars | 5.1570 |
| exposure | 0.1568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
