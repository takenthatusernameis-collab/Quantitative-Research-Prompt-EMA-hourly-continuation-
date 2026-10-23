# EMA Hourly Continuation — CATI/USDT P8_21

**Symbol:** CATI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1421 |
| net_profit_factor | 0.3976 |
| net_win_rate | 0.3786 |
| gross_profit_factor | 0.7034 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -14.3461 |
| sortino_ratio | -8.3990 |
| max_drawdown | 0.9999 |
| cagr | -0.9866 |
| net_avg_win | 12.2685 |
| net_avg_loss | -18.7986 |
| avg_hold_time_bars | 2.9226 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
