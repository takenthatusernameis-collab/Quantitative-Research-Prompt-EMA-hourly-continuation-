# EMA Hourly Continuation — AXS/USDT P20_50

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.8293 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1369 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -1.2696 |
| sortino_ratio | -0.4009 |
| max_drawdown | 0.4135 |
| cagr | -0.1686 |
| net_avg_win | 70.9299 |
| net_avg_loss | -97.3652 |
| avg_hold_time_bars | 8.1106 |
| exposure | 0.1758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
