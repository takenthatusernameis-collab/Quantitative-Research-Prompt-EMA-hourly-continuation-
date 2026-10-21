# EMA Hourly Continuation — KCS/USDT P8_34

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.4103 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.7501 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -6.5458 |
| sortino_ratio | -2.3941 |
| max_drawdown | 0.9402 |
| cagr | -0.6742 |
| net_avg_win | 23.5346 |
| net_avg_loss | -43.5636 |
| avg_hold_time_bars | 10.4084 |
| exposure | 0.3047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
