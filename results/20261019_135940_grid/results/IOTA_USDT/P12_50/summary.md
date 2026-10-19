# EMA Hourly Continuation — IOTA/USDT P12_50

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.5326 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.9411 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -6.9714 |
| sortino_ratio | -3.2490 |
| max_drawdown | 0.9836 |
| cagr | -0.8014 |
| net_avg_win | 21.7034 |
| net_avg_loss | -34.8697 |
| avg_hold_time_bars | 6.8463 |
| exposure | 0.3482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
