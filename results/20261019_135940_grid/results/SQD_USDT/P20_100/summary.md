# EMA Hourly Continuation — SQD/USDT P20_100

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -2.7177 |
| sortino_ratio | -1.0041 |
| max_drawdown | 0.7019 |
| cagr | -0.3808 |
| net_avg_win | 56.5639 |
| net_avg_loss | -75.4053 |
| avg_hold_time_bars | 12.6612 |
| exposure | 0.3969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
