# EMA Hourly Continuation — AKT/USDT P50_200

**Symbol:** AKT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9764 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8549 |
| sortino_ratio | -0.5356 |
| max_drawdown | 0.4829 |
| cagr | -0.2229 |
| net_avg_win | 61.8983 |
| net_avg_loss | -84.5609 |
| avg_hold_time_bars | 19.4324 |
| exposure | 0.3657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
