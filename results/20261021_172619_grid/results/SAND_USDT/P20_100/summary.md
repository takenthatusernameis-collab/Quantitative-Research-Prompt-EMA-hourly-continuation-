# EMA Hourly Continuation — SAND/USDT P20_100

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8668 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -2.8109 |
| sortino_ratio | -0.8489 |
| max_drawdown | 0.6468 |
| cagr | -0.3230 |
| net_avg_win | 64.7086 |
| net_avg_loss | -79.5752 |
| avg_hold_time_bars | 19.5531 |
| exposure | 0.4017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
