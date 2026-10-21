# EMA Hourly Continuation — ROSE/USDT P20_50

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.6077 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 1.0039 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -6.6740 |
| sortino_ratio | -3.0585 |
| max_drawdown | 0.9764 |
| cagr | -0.7689 |
| net_avg_win | 31.5198 |
| net_avg_loss | -43.5123 |
| avg_hold_time_bars | 4.9000 |
| exposure | 0.2339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
