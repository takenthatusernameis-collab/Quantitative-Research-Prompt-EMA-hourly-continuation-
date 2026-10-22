# EMA Hourly Continuation — POL/USDT P21_144

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6331 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5219 |
| sortino_ratio | -0.7404 |
| max_drawdown | 0.6296 |
| cagr | -0.2970 |
| net_avg_win | 47.3458 |
| net_avg_loss | -74.0961 |
| avg_hold_time_bars | 31.7163 |
| exposure | 0.6199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
