# EMA Hourly Continuation — POL/USDT P55_100

**Symbol:** POL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.3343 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.6601 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -6.5274 |
| sortino_ratio | -2.4024 |
| max_drawdown | 0.9503 |
| cagr | -0.6955 |
| net_avg_win | 15.6319 |
| net_avg_loss | -37.7331 |
| avg_hold_time_bars | 5.7892 |
| exposure | 0.1797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
