# EMA Hourly Continuation — ORCA/USDT P21_100

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8077 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0286 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.4733 |
| sortino_ratio | -0.4674 |
| max_drawdown | 0.4774 |
| cagr | -0.1965 |
| net_avg_win | 70.7520 |
| net_avg_loss | -90.8511 |
| avg_hold_time_bars | 18.2657 |
| exposure | 0.4093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
