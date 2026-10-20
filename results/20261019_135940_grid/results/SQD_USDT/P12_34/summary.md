# EMA Hourly Continuation — SQD/USDT P12_34

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1209 |
| net_profit_factor | 0.6316 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9979 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -6.7689 |
| sortino_ratio | -3.3594 |
| max_drawdown | 0.9815 |
| cagr | -0.8058 |
| net_avg_win | 29.8270 |
| net_avg_loss | -41.2956 |
| avg_hold_time_bars | 4.2390 |
| exposure | 0.2409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
