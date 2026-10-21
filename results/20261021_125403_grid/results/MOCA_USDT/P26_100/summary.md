# EMA Hourly Continuation — MOCA/USDT P26_100

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8194 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0511 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -1.5601 |
| sortino_ratio | -0.4927 |
| max_drawdown | 0.4900 |
| cagr | -0.2044 |
| net_avg_win | 82.2431 |
| net_avg_loss | -103.6016 |
| avg_hold_time_bars | 14.5034 |
| exposure | 0.3206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
