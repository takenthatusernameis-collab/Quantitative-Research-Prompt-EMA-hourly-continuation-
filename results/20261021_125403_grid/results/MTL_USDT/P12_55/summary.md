# EMA Hourly Continuation — MTL/USDT P12_55

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.7651 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 1.0428 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -2.7471 |
| sortino_ratio | -0.9898 |
| max_drawdown | 0.7656 |
| cagr | -0.3663 |
| net_avg_win | 70.6611 |
| net_avg_loss | -90.3532 |
| avg_hold_time_bars | 15.4270 |
| exposure | 0.4447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
