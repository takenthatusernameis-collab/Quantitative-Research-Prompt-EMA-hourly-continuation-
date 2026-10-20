# EMA Hourly Continuation — MTL/USDT P8_34

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1254 |
| net_profit_factor | 0.5093 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.9367 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -8.7470 |
| sortino_ratio | -4.3549 |
| max_drawdown | 0.9956 |
| cagr | -0.8827 |
| net_avg_win | 18.8530 |
| net_avg_loss | -28.7344 |
| avg_hold_time_bars | 7.0024 |
| exposure | 0.3974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
