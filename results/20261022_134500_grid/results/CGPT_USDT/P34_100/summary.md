# EMA Hourly Continuation — CGPT/USDT P34_100

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.0322 |
| sortino_ratio | -1.4004 |
| max_drawdown | 0.8199 |
| cagr | -0.4913 |
| net_avg_win | 48.7275 |
| net_avg_loss | -68.3731 |
| avg_hold_time_bars | 9.3912 |
| exposure | 0.2608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
