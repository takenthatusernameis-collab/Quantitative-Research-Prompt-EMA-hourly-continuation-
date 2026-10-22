# EMA Hourly Continuation — AEVO/USDT P12_144

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8078 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -1.2946 |
| sortino_ratio | -0.3334 |
| max_drawdown | 0.4025 |
| cagr | -0.1438 |
| net_avg_win | 85.6557 |
| net_avg_loss | -99.7598 |
| avg_hold_time_bars | 48.1311 |
| exposure | 0.7144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
