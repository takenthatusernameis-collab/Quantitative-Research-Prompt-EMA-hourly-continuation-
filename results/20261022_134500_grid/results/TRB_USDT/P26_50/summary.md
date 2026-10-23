# EMA Hourly Continuation — TRB/USDT P26_50

**Symbol:** TRB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.3774 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.7170 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -9.5958 |
| sortino_ratio | -4.4064 |
| max_drawdown | 0.9961 |
| cagr | -0.8885 |
| net_avg_win | 13.7542 |
| net_avg_loss | -26.0564 |
| avg_hold_time_bars | 3.3837 |
| exposure | 0.1612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
