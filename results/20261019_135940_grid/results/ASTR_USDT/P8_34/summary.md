# EMA Hourly Continuation — ASTR/USDT P8_34

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.4925 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -7.7742 |
| sortino_ratio | -3.8703 |
| max_drawdown | 0.9913 |
| cagr | -0.8472 |
| net_avg_win | 16.8774 |
| net_avg_loss | -28.4319 |
| avg_hold_time_bars | 6.2172 |
| exposure | 0.3537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
