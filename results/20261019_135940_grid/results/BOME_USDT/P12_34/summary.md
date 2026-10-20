# EMA Hourly Continuation — BOME/USDT P12_34

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1325 |
| net_profit_factor | 0.4689 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.7870 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -7.9791 |
| sortino_ratio | -4.0898 |
| max_drawdown | 0.9936 |
| cagr | -0.8628 |
| net_avg_win | 14.9117 |
| net_avg_loss | -25.3731 |
| avg_hold_time_bars | 3.4694 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
