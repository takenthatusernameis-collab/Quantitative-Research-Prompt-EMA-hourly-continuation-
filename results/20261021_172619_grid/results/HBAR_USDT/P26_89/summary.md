# EMA Hourly Continuation — HBAR/USDT P26_89

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7681 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.8657 |
| sortino_ratio | -0.5655 |
| max_drawdown | 0.5091 |
| cagr | -0.2287 |
| net_avg_win | 71.1689 |
| net_avg_loss | -92.2370 |
| avg_hold_time_bars | 12.3423 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
