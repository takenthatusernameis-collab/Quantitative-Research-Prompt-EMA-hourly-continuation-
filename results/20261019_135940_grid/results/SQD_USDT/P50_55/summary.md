# EMA Hourly Continuation — SQD/USDT P50_55

**Symbol:** SQD/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.3495 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.8807 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -9.8733 |
| sortino_ratio | -3.8575 |
| max_drawdown | 0.9936 |
| cagr | -0.8750 |
| net_avg_win | 18.7285 |
| net_avg_loss | -34.2456 |
| avg_hold_time_bars | 2.3037 |
| exposure | 0.0792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
