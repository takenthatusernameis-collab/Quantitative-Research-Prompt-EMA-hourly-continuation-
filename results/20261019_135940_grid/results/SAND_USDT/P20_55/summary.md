# EMA Hourly Continuation — SAND/USDT P20_55

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 863 |
| net_profit_factor | 0.4885 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.9098 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -6.7341 |
| sortino_ratio | -2.7817 |
| max_drawdown | 0.9705 |
| cagr | -0.7461 |
| net_avg_win | 23.5853 |
| net_avg_loss | -40.1819 |
| avg_hold_time_bars | 6.5829 |
| exposure | 0.2582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
