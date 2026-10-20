# EMA Hourly Continuation — AXL/USDT P100_144

**Symbol:** AXL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.5432 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -4.9362 |
| sortino_ratio | -1.6438 |
| max_drawdown | 0.8598 |
| cagr | -0.5381 |
| net_avg_win | 41.6250 |
| net_avg_loss | -61.7546 |
| avg_hold_time_bars | 4.6029 |
| exposure | 0.1143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
