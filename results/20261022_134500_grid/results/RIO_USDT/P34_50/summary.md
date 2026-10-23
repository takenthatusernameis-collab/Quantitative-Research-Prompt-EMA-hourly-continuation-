# EMA Hourly Continuation — RIO/USDT P34_50

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.3624 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 0.6421 |
| gross_win_rate | 0.3827 |
| sharpe_ratio | -10.4561 |
| sortino_ratio | -4.7699 |
| max_drawdown | 0.9975 |
| cagr | -0.9093 |
| net_avg_win | 14.6098 |
| net_avg_loss | -23.9923 |
| avg_hold_time_bars | 2.5096 |
| exposure | 0.1198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
