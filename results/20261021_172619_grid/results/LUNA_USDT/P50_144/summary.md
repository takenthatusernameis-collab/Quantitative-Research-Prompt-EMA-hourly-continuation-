# EMA Hourly Continuation — LUNA/USDT P50_144

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8504 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -2.2840 |
| sortino_ratio | -0.6138 |
| max_drawdown | 0.5121 |
| cagr | -0.2458 |
| net_avg_win | 59.9043 |
| net_avg_loss | -79.0489 |
| avg_hold_time_bars | 14.8876 |
| exposure | 0.2409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
