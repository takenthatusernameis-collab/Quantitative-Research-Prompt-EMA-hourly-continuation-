# EMA Hourly Continuation — BLUR/USDT P34_55

**Symbol:** BLUR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.4915 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9836 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -6.5319 |
| sortino_ratio | -2.7167 |
| max_drawdown | 0.9684 |
| cagr | -0.7421 |
| net_avg_win | 22.2611 |
| net_avg_loss | -41.2628 |
| avg_hold_time_bars | 3.1283 |
| exposure | 0.1247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
