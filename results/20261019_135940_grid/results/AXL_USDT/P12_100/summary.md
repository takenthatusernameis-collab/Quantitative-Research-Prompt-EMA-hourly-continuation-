# EMA Hourly Continuation — AXL/USDT P12_100

**Symbol:** AXL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -5.6406 |
| sortino_ratio | -2.1933 |
| max_drawdown | 0.9333 |
| cagr | -0.6526 |
| net_avg_win | 41.2727 |
| net_avg_loss | -51.7264 |
| avg_hold_time_bars | 15.9045 |
| exposure | 0.5578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
