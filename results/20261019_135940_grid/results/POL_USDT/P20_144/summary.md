# EMA Hourly Continuation — POL/USDT P20_144

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9809 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -2.6587 |
| sortino_ratio | -0.7873 |
| max_drawdown | 0.6477 |
| cagr | -0.3158 |
| net_avg_win | 45.9887 |
| net_avg_loss | -73.2520 |
| avg_hold_time_bars | 31.1041 |
| exposure | 0.6249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
