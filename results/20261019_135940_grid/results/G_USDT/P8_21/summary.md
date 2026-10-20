# EMA Hourly Continuation — G/USDT P8_21

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1205 |
| net_profit_factor | 0.4356 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -9.4138 |
| sortino_ratio | -4.9662 |
| max_drawdown | 0.9952 |
| cagr | -0.9145 |
| net_avg_win | 13.9381 |
| net_avg_loss | -26.9600 |
| avg_hold_time_bars | 4.2855 |
| exposure | 0.2715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
