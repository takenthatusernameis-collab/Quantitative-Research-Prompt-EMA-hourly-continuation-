# EMA Hourly Continuation — IOST/USDT P20_21

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.1091 |
| net_win_rate | 0.2844 |
| gross_profit_factor | 0.6497 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -17.9311 |
| sortino_ratio | -9.5350 |
| max_drawdown | 1.0000 |
| cagr | -0.9947 |
| net_avg_win | 3.6355 |
| net_avg_loss | -13.2372 |
| avg_hold_time_bars | 2.1401 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
