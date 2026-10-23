# EMA Hourly Continuation — ALPINE/USDT P26_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.8005 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0555 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -0.9789 |
| sortino_ratio | -0.2113 |
| max_drawdown | 0.2703 |
| cagr | -0.0949 |
| net_avg_win | 74.7279 |
| net_avg_loss | -100.0740 |
| avg_hold_time_bars | 72.8783 |
| exposure | 0.7619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
