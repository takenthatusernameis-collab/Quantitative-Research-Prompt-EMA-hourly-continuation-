# EMA Hourly Continuation — SHIB/USDT P50_144

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7701 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.4703 |
| sortino_ratio | -0.3856 |
| max_drawdown | 0.3910 |
| cagr | -0.1619 |
| net_avg_win | 71.4391 |
| net_avg_loss | -93.8855 |
| avg_hold_time_bars | 16.3114 |
| exposure | 0.2476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
