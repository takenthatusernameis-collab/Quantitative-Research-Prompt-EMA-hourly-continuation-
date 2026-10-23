# EMA Hourly Continuation — CWEB/USDT P20_34

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.2655 |
| net_win_rate | 0.2561 |
| gross_profit_factor | 0.6313 |
| gross_win_rate | 0.2803 |
| sharpe_ratio | -17.2997 |
| sortino_ratio | -8.5246 |
| max_drawdown | 1.0000 |
| cagr | -0.9912 |
| net_avg_win | 13.1449 |
| net_avg_loss | -17.0398 |
| avg_hold_time_bars | 4.0512 |
| exposure | 0.1978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
