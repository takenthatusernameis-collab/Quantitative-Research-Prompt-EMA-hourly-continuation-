# EMA Hourly Continuation — RAY/USDT P50_100

**Symbol:** RAY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.8632 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1069 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.8018 |
| sortino_ratio | -0.2179 |
| max_drawdown | 0.2972 |
| cagr | -0.0974 |
| net_avg_win | 76.1985 |
| net_avg_loss | -99.3699 |
| avg_hold_time_bars | 8.3268 |
| exposure | 0.1344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
