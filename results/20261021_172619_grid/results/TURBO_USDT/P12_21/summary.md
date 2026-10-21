# EMA Hourly Continuation — TURBO/USDT P12_21

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.9021 |
| net_win_rate | 0.5543 |
| gross_profit_factor | 1.2323 |
| gross_win_rate | 0.5543 |
| sharpe_ratio | -0.5347 |
| sortino_ratio | -0.1392 |
| max_drawdown | 0.1995 |
| cagr | -0.0643 |
| net_avg_win | 80.8315 |
| net_avg_loss | -111.4344 |
| avg_hold_time_bars | 4.2172 |
| exposure | 0.0614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
