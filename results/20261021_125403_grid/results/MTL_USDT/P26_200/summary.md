# EMA Hourly Continuation — MTL/USDT P26_200

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7476 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -1.4610 |
| sortino_ratio | -0.3447 |
| max_drawdown | 0.3463 |
| cagr | -0.1473 |
| net_avg_win | 73.7093 |
| net_avg_loss | -92.3487 |
| avg_hold_time_bars | 50.5018 |
| exposure | 0.6285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
