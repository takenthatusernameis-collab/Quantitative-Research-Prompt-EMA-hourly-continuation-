# EMA Hourly Continuation — EGLD/USDT P12_34

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1275 |
| net_profit_factor | 0.4449 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.9706 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -9.1102 |
| sortino_ratio | -4.5860 |
| max_drawdown | 0.9968 |
| cagr | -0.8972 |
| net_avg_win | 14.1616 |
| net_avg_loss | -25.2519 |
| avg_hold_time_bars | 4.1380 |
| exposure | 0.2398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
