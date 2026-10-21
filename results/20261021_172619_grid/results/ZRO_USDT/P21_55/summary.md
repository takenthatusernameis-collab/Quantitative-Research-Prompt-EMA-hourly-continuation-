# EMA Hourly Continuation — ZRO/USDT P21_55

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.8721 |
| net_win_rate | 0.5207 |
| gross_profit_factor | 1.0782 |
| gross_win_rate | 0.5207 |
| sharpe_ratio | -0.9269 |
| sortino_ratio | -0.3048 |
| max_drawdown | 0.3068 |
| cagr | -0.1341 |
| net_avg_win | 77.1590 |
| net_avg_loss | -96.1047 |
| avg_hold_time_bars | 8.2397 |
| exposure | 0.1952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
