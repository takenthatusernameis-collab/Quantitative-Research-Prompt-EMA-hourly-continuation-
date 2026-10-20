# EMA Hourly Continuation — KNC/USDT P8_34

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.4542 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -8.9737 |
| sortino_ratio | -4.4069 |
| max_drawdown | 0.9957 |
| cagr | -0.8857 |
| net_avg_win | 15.8704 |
| net_avg_loss | -26.3222 |
| avg_hold_time_bars | 6.7630 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
