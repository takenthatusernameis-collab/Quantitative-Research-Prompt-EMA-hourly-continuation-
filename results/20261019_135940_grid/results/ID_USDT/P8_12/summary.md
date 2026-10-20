# EMA Hourly Continuation — ID/USDT P8_12

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1593 |
| net_profit_factor | 0.2553 |
| net_win_rate | 0.3999 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -14.3518 |
| sortino_ratio | -8.1810 |
| max_drawdown | 1.0000 |
| cagr | -0.9856 |
| net_avg_win | 5.3825 |
| net_avg_loss | -14.0465 |
| avg_hold_time_bars | 2.5097 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
