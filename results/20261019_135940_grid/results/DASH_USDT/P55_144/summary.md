# EMA Hourly Continuation — DASH/USDT P55_144

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.4595 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8252 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.7999 |
| sortino_ratio | -1.5797 |
| max_drawdown | 0.8697 |
| cagr | -0.5395 |
| net_avg_win | 29.1532 |
| net_avg_loss | -53.0497 |
| avg_hold_time_bars | 8.6412 |
| exposure | 0.2156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
