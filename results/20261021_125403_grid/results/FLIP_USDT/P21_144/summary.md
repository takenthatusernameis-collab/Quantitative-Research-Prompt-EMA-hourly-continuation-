# EMA Hourly Continuation — FLIP/USDT P21_144

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.2254 |
| sortino_ratio | -0.5841 |
| max_drawdown | 0.5098 |
| cagr | -0.2393 |
| net_avg_win | 65.9461 |
| net_avg_loss | -85.4237 |
| avg_hold_time_bars | 32.8703 |
| exposure | 0.5185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
