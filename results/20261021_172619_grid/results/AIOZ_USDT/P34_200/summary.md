# EMA Hourly Continuation — AIOZ/USDT P34_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8789 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0248 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -0.7561 |
| sortino_ratio | -0.1892 |
| max_drawdown | 0.3383 |
| cagr | -0.0857 |
| net_avg_win | 94.9399 |
| net_avg_loss | -110.1708 |
| avg_hold_time_bars | 36.4361 |
| exposure | 0.5051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
