# EMA Hourly Continuation — PUNDIX/USDT P12_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.8196 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0504 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.2574 |
| sortino_ratio | -0.3581 |
| max_drawdown | 0.3656 |
| cagr | -0.1541 |
| net_avg_win | 77.1982 |
| net_avg_loss | -98.5776 |
| avg_hold_time_bars | 38.1013 |
| exposure | 0.6841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
