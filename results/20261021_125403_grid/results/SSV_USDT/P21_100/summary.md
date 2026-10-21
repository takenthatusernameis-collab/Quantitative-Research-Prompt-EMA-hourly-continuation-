# EMA Hourly Continuation — SSV/USDT P21_100

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7110 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8726 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -2.6991 |
| sortino_ratio | -0.8630 |
| max_drawdown | 0.6621 |
| cagr | -0.3277 |
| net_avg_win | 66.8060 |
| net_avg_loss | -79.0357 |
| avg_hold_time_bars | 17.3059 |
| exposure | 0.3994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
