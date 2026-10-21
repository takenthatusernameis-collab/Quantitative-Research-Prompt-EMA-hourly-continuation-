# EMA Hourly Continuation — TURBO/USDT P20_34

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7918 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.3856 |
| sortino_ratio | -0.3612 |
| max_drawdown | 0.3809 |
| cagr | -0.1531 |
| net_avg_win | 79.7404 |
| net_avg_loss | -105.2229 |
| avg_hold_time_bars | 4.9307 |
| exposure | 0.0737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
