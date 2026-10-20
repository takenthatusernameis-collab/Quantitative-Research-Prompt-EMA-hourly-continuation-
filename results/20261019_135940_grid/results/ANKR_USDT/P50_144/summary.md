# EMA Hourly Continuation — ANKR/USDT P50_144

**Symbol:** ANKR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.5149 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.8689 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -5.1003 |
| sortino_ratio | -1.6116 |
| max_drawdown | 0.8616 |
| cagr | -0.5433 |
| net_avg_win | 41.6905 |
| net_avg_loss | -62.0035 |
| avg_hold_time_bars | 13.7525 |
| exposure | 0.3157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
