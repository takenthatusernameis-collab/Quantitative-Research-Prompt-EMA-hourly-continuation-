# EMA Hourly Continuation — SQD/USDT P100_200

**Symbol:** SQD/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7663 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.5824 |
| sortino_ratio | -0.4430 |
| max_drawdown | 0.4139 |
| cagr | -0.1851 |
| net_avg_win | 67.9678 |
| net_avg_loss | -92.6114 |
| avg_hold_time_bars | 10.2378 |
| exposure | 0.1780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
