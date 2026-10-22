# EMA Hourly Continuation — CETUS/USDT P26_55

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7022 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -2.5693 |
| sortino_ratio | -0.8123 |
| max_drawdown | 0.6198 |
| cagr | -0.3116 |
| net_avg_win | 61.2003 |
| net_avg_loss | -79.3894 |
| avg_hold_time_bars | 6.6268 |
| exposure | 0.1478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
