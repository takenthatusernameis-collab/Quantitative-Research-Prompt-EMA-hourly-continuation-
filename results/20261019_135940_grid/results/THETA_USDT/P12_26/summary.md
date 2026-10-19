# EMA Hourly Continuation — THETA/USDT P12_26

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1381 |
| net_profit_factor | 0.4289 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -10.4565 |
| sortino_ratio | -5.4967 |
| max_drawdown | 0.9990 |
| cagr | -0.9355 |
| net_avg_win | 12.4835 |
| net_avg_loss | -22.4261 |
| avg_hold_time_bars | 2.9203 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
