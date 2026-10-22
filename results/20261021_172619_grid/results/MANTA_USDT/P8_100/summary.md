# EMA Hourly Continuation — MANTA/USDT P8_100

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -1.5594 |
| sortino_ratio | -0.4871 |
| max_drawdown | 0.4970 |
| cagr | -0.2023 |
| net_avg_win | 86.9743 |
| net_avg_loss | -101.9374 |
| avg_hold_time_bars | 31.2218 |
| exposure | 0.6784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
