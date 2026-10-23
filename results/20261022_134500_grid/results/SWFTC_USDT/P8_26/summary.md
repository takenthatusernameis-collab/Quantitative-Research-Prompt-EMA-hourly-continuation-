# EMA Hourly Continuation — SWFTC/USDT P8_26

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1491 |
| net_profit_factor | 0.3803 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.7707 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -11.5701 |
| sortino_ratio | -6.2672 |
| max_drawdown | 0.9997 |
| cagr | -0.9605 |
| net_avg_win | 9.8777 |
| net_avg_loss | -18.5414 |
| avg_hold_time_bars | 3.9826 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
