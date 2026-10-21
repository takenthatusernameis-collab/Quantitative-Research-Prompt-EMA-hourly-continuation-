# EMA Hourly Continuation — SSV/USDT P8_50

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.7658 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -2.8867 |
| sortino_ratio | -1.0965 |
| max_drawdown | 0.7401 |
| cagr | -0.3966 |
| net_avg_win | 70.1183 |
| net_avg_loss | -80.9576 |
| avg_hold_time_bars | 14.5950 |
| exposure | 0.4729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
