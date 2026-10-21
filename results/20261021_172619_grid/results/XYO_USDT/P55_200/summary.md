# EMA Hourly Continuation — XYO/USDT P55_200

**Symbol:** XYO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5984 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.7952 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -2.8777 |
| sortino_ratio | -0.7830 |
| max_drawdown | 0.6177 |
| cagr | -0.3029 |
| net_avg_win | 53.3277 |
| net_avg_loss | -73.6712 |
| avg_hold_time_bars | 20.8238 |
| exposure | 0.3477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
