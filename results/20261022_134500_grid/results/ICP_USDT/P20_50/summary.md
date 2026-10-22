# EMA Hourly Continuation — ICP/USDT P20_50

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.4813 |
| net_win_rate | 0.4555 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -7.3430 |
| sortino_ratio | -3.2582 |
| max_drawdown | 0.9834 |
| cagr | -0.8014 |
| net_avg_win | 19.9971 |
| net_avg_loss | -34.7633 |
| avg_hold_time_bars | 4.6284 |
| exposure | 0.2106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
