# EMA Hourly Continuation — POLYX/USDT P34_144

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.8022 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.4279 |
| sortino_ratio | -0.4002 |
| max_drawdown | 0.4170 |
| cagr | -0.1690 |
| net_avg_win | 78.1003 |
| net_avg_loss | -98.3813 |
| avg_hold_time_bars | 23.4870 |
| exposure | 0.4100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
