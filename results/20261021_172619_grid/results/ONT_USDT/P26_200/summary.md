# EMA Hourly Continuation — ONT/USDT P26_200

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7667 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9201 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -1.4298 |
| sortino_ratio | -0.3580 |
| max_drawdown | 0.4135 |
| cagr | -0.1525 |
| net_avg_win | 75.2854 |
| net_avg_loss | -90.8744 |
| avg_hold_time_bars | 38.1387 |
| exposure | 0.5350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
