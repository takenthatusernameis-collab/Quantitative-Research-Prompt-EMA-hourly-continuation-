# EMA Hourly Continuation — UQC/USDT P8_21

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 789 |
| net_profit_factor | 0.1244 |
| net_win_rate | 0.1939 |
| gross_profit_factor | 0.3764 |
| gross_win_rate | 0.2611 |
| sharpe_ratio | -16.3296 |
| sortino_ratio | -7.1644 |
| max_drawdown | 1.0000 |
| cagr | -0.9817 |
| net_avg_win | 9.2842 |
| net_avg_loss | -17.9561 |
| avg_hold_time_bars | 10.7364 |
| exposure | 0.3834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
