# EMA Hourly Continuation — QNT/USDT P8_21

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7500 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0918 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -2.0099 |
| sortino_ratio | -0.6574 |
| max_drawdown | 0.5726 |
| cagr | -0.2589 |
| net_avg_win | 58.9853 |
| net_avg_loss | -86.7012 |
| avg_hold_time_bars | 5.6842 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
