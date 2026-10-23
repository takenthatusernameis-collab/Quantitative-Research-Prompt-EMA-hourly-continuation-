# EMA Hourly Continuation — TNSR/USDT P12_50

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.6992 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 1.0316 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -4.9869 |
| sortino_ratio | -2.2595 |
| max_drawdown | 0.9384 |
| cagr | -0.6624 |
| net_avg_win | 43.5749 |
| net_avg_loss | -57.2696 |
| avg_hold_time_bars | 7.6574 |
| exposure | 0.3611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
