# EMA Hourly Continuation — RAY/USDT P8_144

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7859 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0589 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -1.8090 |
| sortino_ratio | -0.5882 |
| max_drawdown | 0.5677 |
| cagr | -0.2422 |
| net_avg_win | 68.9462 |
| net_avg_loss | -90.7948 |
| avg_hold_time_bars | 30.2038 |
| exposure | 0.7208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
