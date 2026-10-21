# EMA Hourly Continuation — THETA/USDT P21_55

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6984 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.4390 |
| sortino_ratio | -0.7532 |
| max_drawdown | 0.6014 |
| cagr | -0.2912 |
| net_avg_win | 60.0756 |
| net_avg_loss | -78.6209 |
| avg_hold_time_bars | 8.3426 |
| exposure | 0.1771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
