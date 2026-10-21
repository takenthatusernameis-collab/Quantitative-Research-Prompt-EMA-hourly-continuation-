# EMA Hourly Continuation — ORCA/USDT P20_55

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.7669 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0339 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -2.0277 |
| sortino_ratio | -0.6990 |
| max_drawdown | 0.5717 |
| cagr | -0.2758 |
| net_avg_win | 61.9350 |
| net_avg_loss | -84.1849 |
| avg_hold_time_bars | 8.9394 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
