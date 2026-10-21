# EMA Hourly Continuation — AEVO/USDT P55_144

**Symbol:** AEVO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7825 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.5149 |
| sortino_ratio | -0.4236 |
| max_drawdown | 0.4090 |
| cagr | -0.1781 |
| net_avg_win | 73.9046 |
| net_avg_loss | -92.4992 |
| avg_hold_time_bars | 14.4609 |
| exposure | 0.2513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
