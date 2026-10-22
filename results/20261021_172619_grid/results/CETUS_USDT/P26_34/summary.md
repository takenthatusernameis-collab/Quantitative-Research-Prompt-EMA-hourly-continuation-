# EMA Hourly Continuation — CETUS/USDT P26_34

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.6044 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8533 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -2.8625 |
| sortino_ratio | -0.6481 |
| max_drawdown | 0.5481 |
| cagr | -0.2590 |
| net_avg_win | 72.3483 |
| net_avg_loss | -95.0900 |
| avg_hold_time_bars | 4.4269 |
| exposure | 0.0507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
