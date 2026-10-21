# EMA Hourly Continuation — DEEP/USDT P20_89

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.9480 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1133 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.3218 |
| sortino_ratio | -0.0950 |
| max_drawdown | 0.2839 |
| cagr | -0.0487 |
| net_avg_win | 98.0098 |
| net_avg_loss | -115.7402 |
| avg_hold_time_bars | 20.9139 |
| exposure | 0.3990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
