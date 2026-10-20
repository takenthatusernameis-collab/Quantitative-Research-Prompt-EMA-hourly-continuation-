# EMA Hourly Continuation — DOGS/USDT P50_144

**Symbol:** DOGS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7221 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0375 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.4973 |
| sortino_ratio | -0.7615 |
| max_drawdown | 0.5638 |
| cagr | -0.3047 |
| net_avg_win | 70.4925 |
| net_avg_loss | -97.6167 |
| avg_hold_time_bars | 14.6375 |
| exposure | 0.3106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
