# EMA Hourly Continuation — MAGIC/USDT P89_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5827 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9630 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -3.7359 |
| sortino_ratio | -1.1254 |
| max_drawdown | 0.7405 |
| cagr | -0.4155 |
| net_avg_win | 47.8568 |
| net_avg_loss | -75.1755 |
| avg_hold_time_bars | 6.5265 |
| exposure | 0.1341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
