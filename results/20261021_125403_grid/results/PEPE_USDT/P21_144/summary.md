# EMA Hourly Continuation — PEPE/USDT P21_144

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7825 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9384 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.3042 |
| sortino_ratio | -0.3243 |
| max_drawdown | 0.3142 |
| cagr | -0.1395 |
| net_avg_win | 76.3705 |
| net_avg_loss | -92.5974 |
| avg_hold_time_bars | 40.7401 |
| exposure | 0.5630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
