# EMA Hourly Continuation — ZPAY/USDT P12_55

**Symbol:** ZPAY/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.4800 |
| net_win_rate | 0.3457 |
| gross_profit_factor | 0.6540 |
| gross_win_rate | 0.3470 |
| sharpe_ratio | -7.6497 |
| sortino_ratio | -2.9805 |
| max_drawdown | 0.9728 |
| cagr | -0.7541 |
| net_avg_win | 33.1939 |
| net_avg_loss | -36.5400 |
| avg_hold_time_bars | 11.6837 |
| exposure | 0.4129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
