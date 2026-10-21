# EMA Hourly Continuation — MNT/USDT P21_55

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -2.7601 |
| sortino_ratio | -0.8876 |
| max_drawdown | 0.6552 |
| cagr | -0.3339 |
| net_avg_win | 49.0273 |
| net_avg_loss | -73.7265 |
| avg_hold_time_bars | 9.6799 |
| exposure | 0.2213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
