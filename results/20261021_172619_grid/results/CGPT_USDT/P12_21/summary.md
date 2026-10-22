# EMA Hourly Continuation — CGPT/USDT P12_21

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8199 |
| net_win_rate | 0.5321 |
| gross_profit_factor | 1.1287 |
| gross_win_rate | 0.5321 |
| sharpe_ratio | -1.1036 |
| sortino_ratio | -0.2884 |
| max_drawdown | 0.3303 |
| cagr | -0.1244 |
| net_avg_win | 74.1951 |
| net_avg_loss | -102.9184 |
| avg_hold_time_bars | 5.0795 |
| exposure | 0.0755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
