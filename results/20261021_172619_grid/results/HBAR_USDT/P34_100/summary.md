# EMA Hourly Continuation — HBAR/USDT P34_100

**Symbol:** HBAR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8825 |
| net_win_rate | 0.5394 |
| gross_profit_factor | 1.1599 |
| gross_win_rate | 0.5394 |
| sharpe_ratio | -0.7245 |
| sortino_ratio | -0.2080 |
| max_drawdown | 0.2421 |
| cagr | -0.0935 |
| net_avg_win | 77.4284 |
| net_avg_loss | -102.7663 |
| avg_hold_time_bars | 12.3639 |
| exposure | 0.2209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
