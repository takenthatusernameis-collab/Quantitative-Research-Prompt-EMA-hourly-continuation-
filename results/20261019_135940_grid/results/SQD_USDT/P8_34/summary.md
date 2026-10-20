# EMA Hourly Continuation — SQD/USDT P8_34

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1318 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -6.9889 |
| sortino_ratio | -3.6129 |
| max_drawdown | 0.9865 |
| cagr | -0.8276 |
| net_avg_win | 26.8664 |
| net_avg_loss | -36.3598 |
| avg_hold_time_bars | 4.9135 |
| exposure | 0.3044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
