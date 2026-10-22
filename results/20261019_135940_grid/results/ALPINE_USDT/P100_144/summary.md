# EMA Hourly Continuation — ALPINE/USDT P100_144

**Symbol:** ALPINE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.4623 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -6.0953 |
| sortino_ratio | -2.0057 |
| max_drawdown | 0.9167 |
| cagr | -0.6268 |
| net_avg_win | 33.3697 |
| net_avg_loss | -56.5914 |
| avg_hold_time_bars | 6.0149 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
