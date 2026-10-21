# EMA Hourly Continuation — POL/USDT P12_50

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.5571 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.7459 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -3.8093 |
| sortino_ratio | -1.2748 |
| max_drawdown | 0.7857 |
| cagr | -0.4440 |
| net_avg_win | 39.4270 |
| net_avg_loss | -56.5220 |
| avg_hold_time_bars | 14.2202 |
| exposure | 0.3581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
