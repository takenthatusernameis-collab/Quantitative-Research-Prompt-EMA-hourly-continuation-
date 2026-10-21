# EMA Hourly Continuation — VELO/USDT P8_12

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.9006 |
| net_win_rate | 0.5431 |
| gross_profit_factor | 1.1809 |
| gross_win_rate | 0.5431 |
| sharpe_ratio | -0.4379 |
| sortino_ratio | -0.0891 |
| max_drawdown | 0.2108 |
| cagr | -0.0416 |
| net_avg_win | 85.6892 |
| net_avg_loss | -113.1173 |
| avg_hold_time_bars | 5.8832 |
| exposure | 0.0527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
