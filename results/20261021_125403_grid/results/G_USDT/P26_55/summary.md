# EMA Hourly Continuation — G/USDT P26_55

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6405 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9350 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.7571 |
| sortino_ratio | -1.2793 |
| max_drawdown | 0.7275 |
| cagr | -0.4434 |
| net_avg_win | 55.9840 |
| net_avg_loss | -76.9893 |
| avg_hold_time_bars | 7.8630 |
| exposure | 0.2022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
