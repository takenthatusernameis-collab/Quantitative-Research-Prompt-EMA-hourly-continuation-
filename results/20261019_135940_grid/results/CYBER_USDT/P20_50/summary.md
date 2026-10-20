# EMA Hourly Continuation — CYBER/USDT P20_50

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -6.8832 |
| sortino_ratio | -2.9892 |
| max_drawdown | 0.9735 |
| cagr | -0.7637 |
| net_avg_win | 27.9372 |
| net_avg_loss | -41.1519 |
| avg_hold_time_bars | 5.9407 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
