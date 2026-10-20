# EMA Hourly Continuation — ELON/USDT P12_26

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1314 |
| net_profit_factor | 0.3081 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.6911 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -11.3649 |
| sortino_ratio | -5.8813 |
| max_drawdown | 0.9994 |
| cagr | -0.9466 |
| net_avg_win | 8.2427 |
| net_avg_loss | -18.6624 |
| avg_hold_time_bars | 3.1842 |
| exposure | 0.1902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
