# EMA Hourly Continuation — EWT/USDT P21_50

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8326 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -3.0317 |
| sortino_ratio | -0.8738 |
| max_drawdown | 0.6393 |
| cagr | -0.3313 |
| net_avg_win | 57.9768 |
| net_avg_loss | -76.1940 |
| avg_hold_time_bars | 7.8418 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
