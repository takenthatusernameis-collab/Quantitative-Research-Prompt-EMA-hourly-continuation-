# EMA Hourly Continuation — WEMIX/USDT P8_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.5345 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.6799 |
| gross_win_rate | 0.3949 |
| sharpe_ratio | -5.2323 |
| sortino_ratio | -1.7949 |
| max_drawdown | 0.8801 |
| cagr | -0.5658 |
| net_avg_win | 43.2123 |
| net_avg_loss | -52.7672 |
| avg_hold_time_bars | 15.6017 |
| exposure | 0.4184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
