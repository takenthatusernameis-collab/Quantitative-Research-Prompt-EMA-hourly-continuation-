# EMA Hourly Continuation — TNSR/USDT P26_34

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6755 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9780 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.2394 |
| sortino_ratio | -0.5377 |
| max_drawdown | 0.5065 |
| cagr | -0.2186 |
| net_avg_win | 69.8548 |
| net_avg_loss | -99.1086 |
| avg_hold_time_bars | 4.3369 |
| exposure | 0.0553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
