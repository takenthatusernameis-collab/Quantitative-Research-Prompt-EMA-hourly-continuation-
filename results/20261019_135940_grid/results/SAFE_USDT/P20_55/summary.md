# EMA Hourly Continuation — SAFE/USDT P20_55

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.5540 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -5.6505 |
| sortino_ratio | -2.4356 |
| max_drawdown | 0.9474 |
| cagr | -0.6895 |
| net_avg_win | 26.7012 |
| net_avg_loss | -43.1031 |
| avg_hold_time_bars | 6.0687 |
| exposure | 0.2590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
