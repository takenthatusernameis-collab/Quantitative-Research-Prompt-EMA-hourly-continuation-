# EMA Hourly Continuation — PENDLE/USDT P8_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8895 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -5.6882 |
| sortino_ratio | -2.6574 |
| max_drawdown | 0.9588 |
| cagr | -0.7190 |
| net_avg_win | 26.7485 |
| net_avg_loss | -39.3741 |
| avg_hold_time_bars | 8.9837 |
| exposure | 0.4512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
