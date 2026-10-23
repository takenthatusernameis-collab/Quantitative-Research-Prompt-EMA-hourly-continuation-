# EMA Hourly Continuation — W/USDT P21_26

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1208 |
| net_profit_factor | 0.3546 |
| net_win_rate | 0.3990 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -12.5465 |
| sortino_ratio | -6.2424 |
| max_drawdown | 0.9997 |
| cagr | -0.9630 |
| net_avg_win | 11.3947 |
| net_avg_loss | -21.3357 |
| avg_hold_time_bars | 1.9495 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
