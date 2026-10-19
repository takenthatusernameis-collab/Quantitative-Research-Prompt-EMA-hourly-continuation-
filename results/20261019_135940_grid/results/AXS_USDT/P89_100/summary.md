# EMA Hourly Continuation — AXS/USDT P89_100

**Symbol:** AXS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.2898 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.8334 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -8.6299 |
| sortino_ratio | -2.9084 |
| max_drawdown | 0.9808 |
| cagr | -0.7892 |
| net_avg_win | 18.3493 |
| net_avg_loss | -42.0830 |
| avg_hold_time_bars | 2.0147 |
| exposure | 0.0498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
