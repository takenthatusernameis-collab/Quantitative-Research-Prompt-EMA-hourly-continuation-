# EMA Hourly Continuation — MTL/USDT P26_55

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 828 |
| net_profit_factor | 0.4841 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.9347 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -7.3887 |
| sortino_ratio | -2.9986 |
| max_drawdown | 0.9769 |
| cagr | -0.7708 |
| net_avg_win | 25.5713 |
| net_avg_loss | -40.2367 |
| avg_hold_time_bars | 6.8973 |
| exposure | 0.2584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
