# EMA Hourly Continuation — MINA/USDT P12_21

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9623 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -2.6985 |
| sortino_ratio | -0.8181 |
| max_drawdown | 0.6643 |
| cagr | -0.3132 |
| net_avg_win | 51.4303 |
| net_avg_loss | -78.2361 |
| avg_hold_time_bars | 4.8453 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
