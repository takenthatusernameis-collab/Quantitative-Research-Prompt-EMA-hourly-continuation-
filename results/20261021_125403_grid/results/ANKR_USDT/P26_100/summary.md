# EMA Hourly Continuation — ANKR/USDT P26_100

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -3.1885 |
| sortino_ratio | -1.0206 |
| max_drawdown | 0.7038 |
| cagr | -0.3759 |
| net_avg_win | 59.5621 |
| net_avg_loss | -76.2558 |
| avg_hold_time_bars | 15.7668 |
| exposure | 0.3626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
