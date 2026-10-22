# EMA Hourly Continuation — XTZ/USDT P8_50

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.5118 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9707 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -6.7944 |
| sortino_ratio | -3.1921 |
| max_drawdown | 0.9804 |
| cagr | -0.7912 |
| net_avg_win | 19.4682 |
| net_avg_loss | -33.7539 |
| avg_hold_time_bars | 9.0276 |
| exposure | 0.4608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
