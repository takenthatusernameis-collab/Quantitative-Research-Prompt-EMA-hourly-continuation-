# EMA Hourly Continuation — XYO/USDT P8_12

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.5585 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8559 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -3.6806 |
| sortino_ratio | -0.9633 |
| max_drawdown | 0.6736 |
| cagr | -0.3584 |
| net_avg_win | 56.7988 |
| net_avg_loss | -82.4644 |
| avg_hold_time_bars | 5.2149 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
