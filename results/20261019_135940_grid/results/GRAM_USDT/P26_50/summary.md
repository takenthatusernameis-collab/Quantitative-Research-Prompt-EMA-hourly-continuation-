# EMA Hourly Continuation — GRAM/USDT P26_50

**Symbol:** GRAM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.3282 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8558 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -10.4406 |
| sortino_ratio | -4.7219 |
| max_drawdown | 0.9976 |
| cagr | -0.9090 |
| net_avg_win | 11.7172 |
| net_avg_loss | -25.2123 |
| avg_hold_time_bars | 3.4060 |
| exposure | 0.1556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
