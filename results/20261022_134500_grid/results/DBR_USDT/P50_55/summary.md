# EMA Hourly Continuation — DBR/USDT P50_55

**Symbol:** DBR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.2729 |
| net_win_rate | 0.3519 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4374 |
| sharpe_ratio | -10.6574 |
| sortino_ratio | -3.9378 |
| max_drawdown | 0.9850 |
| cagr | -0.8746 |
| net_avg_win | 20.8811 |
| net_avg_loss | -41.5374 |
| avg_hold_time_bars | 3.8807 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
