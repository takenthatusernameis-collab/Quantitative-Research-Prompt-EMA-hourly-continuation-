# EMA Hourly Continuation — AURORA/USDT P26_34

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.2500 |
| net_win_rate | 0.3499 |
| gross_profit_factor | 0.7871 |
| gross_win_rate | 0.3987 |
| sharpe_ratio | -12.9172 |
| sortino_ratio | -5.7288 |
| max_drawdown | 0.9996 |
| cagr | -0.9525 |
| net_avg_win | 10.5422 |
| net_avg_loss | -22.7029 |
| avg_hold_time_bars | 3.2049 |
| exposure | 0.1315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
