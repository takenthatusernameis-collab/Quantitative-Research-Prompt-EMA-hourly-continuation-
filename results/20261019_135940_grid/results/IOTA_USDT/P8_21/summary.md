# EMA Hourly Continuation — IOTA/USDT P8_21

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1709 |
| net_profit_factor | 0.3132 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.7879 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -11.5908 |
| sortino_ratio | -6.7675 |
| max_drawdown | 0.9998 |
| cagr | -0.9662 |
| net_avg_win | 6.0539 |
| net_avg_loss | -15.2266 |
| avg_hold_time_bars | 3.0568 |
| exposure | 0.2375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
