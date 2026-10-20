# EMA Hourly Continuation — SSV/USDT P20_34

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.4118 |
| net_win_rate | 0.4104 |
| gross_profit_factor | 0.7855 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -10.5515 |
| sortino_ratio | -5.2572 |
| max_drawdown | 0.9986 |
| cagr | -0.9258 |
| net_avg_win | 13.8140 |
| net_avg_loss | -23.3504 |
| avg_hold_time_bars | 2.8345 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
