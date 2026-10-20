# EMA Hourly Continuation — ORCA/USDT P50_200

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.0840 |
| sortino_ratio | -0.8586 |
| max_drawdown | 0.6771 |
| cagr | -0.3363 |
| net_avg_win | 46.4679 |
| net_avg_loss | -72.5792 |
| avg_hold_time_bars | 21.4898 |
| exposure | 0.3829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
