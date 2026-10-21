# EMA Hourly Continuation — ELON/USDT P20_100

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7532 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.0330 |
| sortino_ratio | -0.6375 |
| max_drawdown | 0.5585 |
| cagr | -0.2541 |
| net_avg_win | 67.9706 |
| net_avg_loss | -85.1448 |
| avg_hold_time_bars | 15.7386 |
| exposure | 0.3448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
