# EMA Hourly Continuation — HNT/USDT P12_26

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8465 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -3.2363 |
| sortino_ratio | -0.9549 |
| max_drawdown | 0.6664 |
| cagr | -0.3541 |
| net_avg_win | 59.4283 |
| net_avg_loss | -76.5138 |
| avg_hold_time_bars | 6.3930 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
