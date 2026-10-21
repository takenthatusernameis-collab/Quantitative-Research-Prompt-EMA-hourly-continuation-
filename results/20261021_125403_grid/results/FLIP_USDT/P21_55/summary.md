# EMA Hourly Continuation — FLIP/USDT P21_55

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -3.0783 |
| sortino_ratio | -0.9262 |
| max_drawdown | 0.6689 |
| cagr | -0.3503 |
| net_avg_win | 52.9593 |
| net_avg_loss | -79.5288 |
| avg_hold_time_bars | 12.5781 |
| exposure | 0.2561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
