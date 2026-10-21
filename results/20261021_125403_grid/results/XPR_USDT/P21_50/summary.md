# EMA Hourly Continuation — XPR/USDT P21_50

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7306 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9886 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.7890 |
| sortino_ratio | -0.4561 |
| max_drawdown | 0.4413 |
| cagr | -0.1885 |
| net_avg_win | 70.5137 |
| net_avg_loss | -95.2962 |
| avg_hold_time_bars | 10.7690 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
