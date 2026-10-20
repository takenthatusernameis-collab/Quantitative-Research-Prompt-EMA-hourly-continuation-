# EMA Hourly Continuation — RSR/USDT P26_100

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.7022 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9706 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.2372 |
| sortino_ratio | -1.1551 |
| max_drawdown | 0.7560 |
| cagr | -0.4206 |
| net_avg_win | 57.6690 |
| net_avg_loss | -75.4489 |
| avg_hold_time_bars | 11.5133 |
| exposure | 0.3334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
