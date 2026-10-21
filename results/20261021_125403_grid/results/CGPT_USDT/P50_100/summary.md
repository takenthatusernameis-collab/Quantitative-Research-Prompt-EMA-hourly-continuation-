# EMA Hourly Continuation — CGPT/USDT P50_100

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7880 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0083 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.3957 |
| sortino_ratio | -0.3788 |
| max_drawdown | 0.3611 |
| cagr | -0.1606 |
| net_avg_win | 73.4642 |
| net_avg_loss | -94.2713 |
| avg_hold_time_bars | 9.6229 |
| exposure | 0.1566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
