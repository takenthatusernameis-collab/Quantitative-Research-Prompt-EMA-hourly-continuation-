# EMA Hourly Continuation — FLOW/USDT P8_55

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.6924 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8963 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.0432 |
| sortino_ratio | -1.1582 |
| max_drawdown | 0.7528 |
| cagr | -0.4127 |
| net_avg_win | 49.2500 |
| net_avg_loss | -63.5796 |
| avg_hold_time_bars | 14.2185 |
| exposure | 0.4615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
