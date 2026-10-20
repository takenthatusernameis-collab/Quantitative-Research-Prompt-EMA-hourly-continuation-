# EMA Hourly Continuation — DIA/USDT P8_50

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.4953 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.7973 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -6.5823 |
| sortino_ratio | -3.0433 |
| max_drawdown | 0.9751 |
| cagr | -0.7675 |
| net_avg_win | 19.7253 |
| net_avg_loss | -32.2986 |
| avg_hold_time_bars | 9.2632 |
| exposure | 0.4540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
