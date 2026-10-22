# EMA Hourly Continuation — ONDO/USDT P21_100

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.6025 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8743 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -4.7138 |
| sortino_ratio | -1.7267 |
| max_drawdown | 0.8857 |
| cagr | -0.5724 |
| net_avg_win | 42.2888 |
| net_avg_loss | -59.3020 |
| avg_hold_time_bars | 11.4565 |
| exposure | 0.3593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
