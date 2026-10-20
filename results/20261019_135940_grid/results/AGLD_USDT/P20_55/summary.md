# EMA Hourly Continuation — AGLD/USDT P20_55

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.5385 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.8625 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -6.5802 |
| sortino_ratio | -2.8516 |
| max_drawdown | 0.9694 |
| cagr | -0.7445 |
| net_avg_win | 27.2837 |
| net_avg_loss | -39.2796 |
| avg_hold_time_bars | 6.4230 |
| exposure | 0.2756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
