# EMA Hourly Continuation — CGPT/USDT P21_34

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.4097 |
| net_win_rate | 0.4179 |
| gross_profit_factor | 0.9064 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -9.8223 |
| sortino_ratio | -4.5088 |
| max_drawdown | 0.9969 |
| cagr | -0.8978 |
| net_avg_win | 15.7976 |
| net_avg_loss | -27.6833 |
| avg_hold_time_bars | 2.6813 |
| exposure | 0.1277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
