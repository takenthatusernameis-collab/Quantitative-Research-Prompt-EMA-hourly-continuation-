# EMA Hourly Continuation — MTL/USDT P21_50

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.6430 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.7321 |
| sortino_ratio | -1.2732 |
| max_drawdown | 0.7871 |
| cagr | -0.4453 |
| net_avg_win | 51.2461 |
| net_avg_loss | -72.5010 |
| avg_hold_time_bars | 9.8196 |
| exposure | 0.2537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
