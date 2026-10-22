# EMA Hourly Continuation — AERO/USDT P34_89

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.5792 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8639 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -3.9729 |
| sortino_ratio | -1.3596 |
| max_drawdown | 0.8086 |
| cagr | -0.4806 |
| net_avg_win | 40.2465 |
| net_avg_loss | -60.1194 |
| avg_hold_time_bars | 8.0655 |
| exposure | 0.2181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
