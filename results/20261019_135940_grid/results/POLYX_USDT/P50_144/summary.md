# EMA Hourly Continuation — POLYX/USDT P50_144

**Symbol:** POLYX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.9176 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.5535 |
| sortino_ratio | -1.0830 |
| max_drawdown | 0.7315 |
| cagr | -0.4020 |
| net_avg_win | 48.6030 |
| net_avg_loss | -72.4462 |
| avg_hold_time_bars | 13.7210 |
| exposure | 0.2906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
