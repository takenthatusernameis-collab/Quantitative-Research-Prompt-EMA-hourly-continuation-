# EMA Hourly Continuation — ROSE/USDT P50_89

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7249 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.0454 |
| sortino_ratio | -0.5601 |
| max_drawdown | 0.5137 |
| cagr | -0.2268 |
| net_avg_win | 70.8217 |
| net_avg_loss | -91.0198 |
| avg_hold_time_bars | 7.8065 |
| exposure | 0.1302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
