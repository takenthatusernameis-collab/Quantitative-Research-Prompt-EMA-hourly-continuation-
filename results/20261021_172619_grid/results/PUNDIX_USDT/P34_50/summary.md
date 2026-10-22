# EMA Hourly Continuation — PUNDIX/USDT P34_50

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0377 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.9163 |
| sortino_ratio | -0.8297 |
| max_drawdown | 0.6233 |
| cagr | -0.3142 |
| net_avg_win | 53.9500 |
| net_avg_loss | -86.0612 |
| avg_hold_time_bars | 5.8462 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
