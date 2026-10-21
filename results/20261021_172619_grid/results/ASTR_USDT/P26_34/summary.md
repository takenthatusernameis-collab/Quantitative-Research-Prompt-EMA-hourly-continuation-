# EMA Hourly Continuation — ASTR/USDT P26_34

**Symbol:** ASTR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6272 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0692 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.6590 |
| sortino_ratio | -0.6520 |
| max_drawdown | 0.5519 |
| cagr | -0.2621 |
| net_avg_win | 60.8616 |
| net_avg_loss | -98.3723 |
| avg_hold_time_bars | 5.5136 |
| exposure | 0.0734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
