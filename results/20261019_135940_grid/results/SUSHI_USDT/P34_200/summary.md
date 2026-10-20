# EMA Hourly Continuation — SUSHI/USDT P34_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6233 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.7016 |
| sortino_ratio | -0.7617 |
| max_drawdown | 0.6113 |
| cagr | -0.3012 |
| net_avg_win | 51.5613 |
| net_avg_loss | -75.9590 |
| avg_hold_time_bars | 27.9474 |
| exposure | 0.5046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
