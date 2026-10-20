# EMA Hourly Continuation — ORCA/USDT P55_89

**Symbol:** ORCA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.4937 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8924 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -5.2554 |
| sortino_ratio | -1.8311 |
| max_drawdown | 0.8974 |
| cagr | -0.5898 |
| net_avg_win | 30.5644 |
| net_avg_loss | -54.1234 |
| avg_hold_time_bars | 5.0295 |
| exposure | 0.1397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
